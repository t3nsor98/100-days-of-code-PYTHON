from fastapi import FastAPI, APIRouter, HTTPException
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import pandas as pd
import json
from motor.motor_asyncio import AsyncIOMotorClient

# Create FastAPI app instance
app = FastAPI()

# Create router instance
router = APIRouter()

# MongoDB connection setup (replace with your connection string)
client = AsyncIOMotorClient(
    'mongodb://LoggerUser:##LoggerDBPass##@10.25.4.25:27017/?authSource=LoggerDB&authMechanism=SCRAM-SHA-1&directConnection=true'
)


def getCollection(collection_name: str):
    """Helper function to get MongoDB collection"""
    db = client["your_database_name"]
    return db[collection_name]


@router.get("/getsendmail")
async def get_send_mail() -> Dict:
    """
    Retrieve and analyze communication data for the last 5 days.
    Returns aggregated statistics for different communication channels.
    """
    try:
        # Time window calculation
        end_time = datetime.now().replace(hour=0, minute=0, second=0)
        start_time = end_time - timedelta(days=5)

        # Define communication types
        COMM_TYPES = [
            "Chat",
            "SMS",
            "Email",
            "Ticket",
            "Whatsapp",
            "LeadData",
            "InboundCallData",
        ]

        # Get data from database
        collection = getCollection("CommData")
        result = await collection.find(
            {
                "type": {"$in": COMM_TYPES},
                "startTime": {"$gte": start_time, "$lt": end_time},
            },
            {"_id": 0},
        ).to_list(length=None)

        # Process data
        data = []
        for doc in result:
            data.extend(json.loads(doc["data"]))

        if not data:
            return {"data": [], "message": "No data found for the specified period"}

        # Convert to DataFrame
        data_df = pd.DataFrame(data)

        # Calculate averages for each channel
        channel_averages = {}
        current_metrics = {}

        for channel in COMM_TYPES:
            channel_data = data_df[data_df["type"] == channel]

            # Calculate 5-day average
            channel_averages[channel] = (
                channel_data["count"].mean() if not channel_data.empty else 0
            )

            # Calculate current day metrics
            current_day_data = channel_data[
                pd.to_datetime(channel_data["ChatDate"]).dt.date
                == datetime.now().date()
            ]
            current_metrics[channel] = (
                current_day_data["count"].sum() if not current_day_data.empty else 0
            )

        # Generate insights
        insights = []
        for channel in COMM_TYPES:
            if channel_averages[channel] > 0:  # Only generate insights if we have data
                if current_metrics[channel] > channel_averages[channel]:
                    insights.append(
                        f"{channel} volume ({current_metrics[channel]:.1f}) is above the 5-day average ({channel_averages[channel]:.1f})"
                    )
                elif current_metrics[channel] < channel_averages[channel]:
                    insights.append(
                        f"{channel} volume ({current_metrics[channel]:.1f}) is below the 5-day average ({channel_averages[channel]:.1f})"
                    )

        # Process detailed current day data
        if not data_df.empty:
            data_df["ChatDate"] = pd.to_datetime(data_df["ChatDate"]).dt.date
            current_detailed = (
                data_df.groupby(["ChatDate", "ProductName", "Status", "type"])["count"]
                .sum()
                .reset_index()
            )
        else:
            current_detailed = pd.DataFrame()

        return {
            "data": data_df.to_dict("records") if not data_df.empty else [],
            "averages": channel_averages,
            "current_metrics": current_metrics,
            "insights": insights,
            "detailed_metrics": (
                current_detailed.to_dict("records")
                if not current_detailed.empty
                else []
            ),
        }

    except Exception as ex:
        print(f"Error occurred: {str(ex)}")  # For debugging
        raise HTTPException(
            status_code=500, detail=f"Error processing communication data: {str(ex)}"
        )


# Include router in the app
app.include_router(router)

# If you're running this directly
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
