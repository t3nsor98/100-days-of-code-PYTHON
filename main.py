from datetime import datetime, timedelta
from fastapi import APIRouter
import pandas as pd
import json

# import DB
from database import getCollection

router = APIRouter()


@router.get("/getsendmail")
def GetSendMail():
    # Get the current date and calculate start and end time
    endTime = datetime.now().replace(hour=0, minute=0, second=0)
    startTime = endTime + timedelta(days=-5)
    startTime = startTime.replace(hour=0, minute=0, second=0)

    print("Start Time:", startTime)
    print("End Time:", endTime)

    try:
        # Get demo data directly from the modified getCollection function
        data = getCollection("CommData")

        # Convert the demo data into a pandas DataFrame
        data_df = pd.DataFrame(data)

        # Check if 'count' column exists
        if "count" not in data_df.columns:
            print("Error: 'count' column not found in the data.")
            return {"error": "'count' column not found in the data."}

        # Print the structure of the DataFrame for debugging
        print("Data Structure:", data_df.head())

        # Ensure startTime and endTime are applied to the data for the last 5 days
        data_df["startTime"] = pd.to_datetime(data_df["startTime"])
        data_df = data_df[
            (data_df["startTime"] >= startTime) & (data_df["startTime"] < endTime)
        ]

        # Calculate averages for the last 5 days
        average_chat_5_days = data_df[data_df["type"] == "Chat"]["count"].mean()
        average_sms_5_days = data_df[data_df["type"] == "SMS"]["count"].mean()
        average_email_5_days = data_df[data_df["type"] == "Email"]["count"].mean()
        average_ticket_5_days = data_df[data_df["type"] == "Ticket"]["count"].mean()
        average_whatsapp_5_days = data_df[data_df["type"] == "WhatsApp"]["count"].mean()
        average_leaddata_5_days = data_df[data_df["type"] == "LeadData"]["count"].mean()
        average_inboundcall_5_days = data_df[data_df["type"] == "InboundCall"][
            "count"
        ].mean()

        print("Averages for the last 5 days:")
        print("Chat:", average_chat_5_days)
        print("SMS:", average_sms_5_days)
        print("Email:", average_email_5_days)
        print("Ticket:", average_ticket_5_days)
        print("WhatsApp:", average_whatsapp_5_days)
        print("LeadData:", average_leaddata_5_days)
        print("InboundCall:", average_inboundcall_5_days)

        # For current data, you can work with the same data, simulating "today's data"
        current_data_df = data_df.copy()

        # Calculate current totals by type (total count for today)
        current_totals = current_data_df.groupby("type")["count"].sum()

        # Prepare the comparison messages based on current totals and 5-day averages
        comparisons = {}

        if current_totals.get("Chat", 0) > average_chat_5_days:
            comparisons["Chat"] = "Chat count has increased in the last 5 days."
        if current_totals.get("SMS", 0) > average_sms_5_days:
            comparisons["SMS"] = "SMS count has increased in the last 5 days."
        if current_totals.get("Email", 0) > average_email_5_days:
            comparisons["Email"] = "Email count has increased in the last 5 days."
        if current_totals.get("Ticket", 0) > average_ticket_5_days:
            comparisons["Ticket"] = "Ticket count has increased in the last 5 days."
        if current_totals.get("WhatsApp", 0) > average_whatsapp_5_days:
            comparisons["WhatsApp"] = "WhatsApp count has increased in the last 5 days."
        if current_totals.get("LeadData", 0) > average_leaddata_5_days:
            comparisons["LeadData"] = "LeadData count has increased in the last 5 days."
        if current_totals.get("InboundCall", 0) > average_inboundcall_5_days:
            comparisons["InboundCall"] = (
                "InboundCall count has increased in the last 5 days."
            )

        # Return data along with comparisons
        return {
            "data": data,
            "averages": {
                "Chat": average_chat_5_days,
                "SMS": average_sms_5_days,
                "Email": average_email_5_days,
                "Ticket": average_ticket_5_days,
                "WhatsApp": average_whatsapp_5_days,
                "LeadData": average_leaddata_5_days,
                "InboundCall": average_inboundcall_5_days,
            },
            "current_totals": current_totals.to_dict(),
            "comparisons": comparisons,
        }

    except Exception as ex:
        print("Error:", ex)
        return {"error": str(ex)}
