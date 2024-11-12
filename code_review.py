from datetime import datetime, timedelta
from typing import Dict, List, Optional
import pandas as pd
from fastapi import HTTPException

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
        
        # Define communication types once
        COMM_TYPES = ['Chat', 'SMS', 'Email', 'Ticket', 'Whatsapp', 'LeadData', 'InboundCallData']
        
        # Get data from database
        data_df = await fetch_communication_data(start_time, end_time, COMM_TYPES)
        if data_df.empty:
            return {"data": [], "message": "No data found for the specified period"}
            
        # Calculate averages
        averages = calculate_channel_averages(data_df)
        
        # Process current day metrics
        current_metrics = process_current_data(data_df)
        
        # Compare with averages and generate insights
        insights = generate_insights(current_metrics, averages)
        
        return {
            "data": data_df.to_dict('records'),
            "averages": averages,
            "current_metrics": current_metrics,
            "insights": insights
        }
        
    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing communication data: {str(ex)}"
        )

async def fetch_communication_data(start_time: datetime, end_time: datetime, comm_types: List[str]) -> pd.DataFrame:
    """Fetch communication data from database and convert to DataFrame."""
    collection = getCollection("CommData")
    result = collection.find(
        {
            'type': {'$in': comm_types},
            'startTime': {'$gte': start_time, '$lt': end_time}
        },
        {'_id': 0}
    )
    
    # Flatten the data
    data = []
    for doc in await result.to_list(length=None):
        data.extend(json.loads(doc['data']))
    
    return pd.DataFrame(data)

def calculate_channel_averages(df: pd.DataFrame) -> Dict[str, float]:
    """Calculate average counts for each communication channel."""
    return {
        channel: df[df['type'] == channel]['count'].mean()
        for channel in df['type'].unique()
    }

def process_current_data(df: pd.DataFrame) -> pd.DataFrame:
    """Process current day data with date grouping."""
    df = df.copy()
    df['ChatDate'] = pd.to_datetime(df['ChatDate']).dt.date
    return df.groupby(['ChatDate', 'ProductName', 'Status', 'type'])['count'].sum().reset_index()

def generate_insights(current_metrics: pd.DataFrame, averages: Dict[str, float]) -> List[str]:
    """Generate insights by comparing current metrics with averages."""
    insights = []
    for channel, avg in averages.items():
        current_val = current_metrics[current_metrics['type'] == channel]['count'].sum()
        if current_val > avg:
            insights.append(f"{channel} volume ({current_val:.1f}) is above the 5-day average ({avg:.1f})")
        elif current_val < avg:
            insights.append(f"{channel} volume ({current_val:.1f}) is below the 5-day average ({avg:.1f})")
    
    return insights