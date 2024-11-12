from datetime import datetime, timedelta
from fastapi import APIRouter

router = APIRouter()
@router.get("/getsendmail")
def GetSendMail():
    endTime = datetime.now().replace(hour=0, minute=0, second=0)
    startTime = endTime + timedelta(days=-5)
    startTime = startTime.replace(hour=0, minute=0, second=0)
    last_5_days = endTime - timedelta(days=5)
    query = {"date": {"$gte": startTime, "$lt": endTime}}
    print(startTime, endTime)
    try:
        collection = getCollection("CommData")
        result = collection.find(
            {
                "type": {
                    "$in": [
                        "Chat",
                        "SMS",
                        "Email",
                        "Ticket",
                        "Whatsapp",
                        "LeadData",
                        "InboundCallData",
                    ]
                },
                "startTime": {"$gte": startTime, "$lt": endTime},
            },
            {"_id": 0},
        )
        data = []
        # print(list(result))
        for doc in list(result):
            data += json.loads(doc["data"])

        # data = pd.DataFrame(data)
        data_df = pd.DataFrame(data)

        # types = ['Chat', 'SMS', 'Email', 'Ticket', 'Whatsapp', 'LeadData', 'InboundCallData']

        # for type in types:
        #     type_data = data_df[data_df['type'] == type]
        #     print(f"Last 5 days ka {type} data:")
        #     print(type_data)
        print("Data for the last 5 days:", data_df.columns)
        print("========================================================")

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

        current_result = collection.find(
            {
                "type": {
                    "$in": [
                        "Chat",
                        "SMS",
                        "Email",
                        "Ticket",
                        "Whatsapp",
                        "LeadData",
                        "InboundCallData",
                    ]
                },
                "startTime": {"$gte": startTime, "$lt": endTime},
            },
            {"_id": 0},
        )

        current_data = []
        print(list(current_result))
        for doc in list(current_result):
            current_data += json.loads(doc["data"])
        average_chat_current = current_data[current_data["type"] == "Chat"][
            "count"
        ].sum()
        average_sms_current = current_data[current_data["type"] == "SMS"]["count"].sum()
        average_email_current = current_data[current_data["type"] == "Email"][
            "count"
        ].sum()
        average_ticket_current = current_data[current_data["type"] == "Ticket"][
            "count"
        ].sum()
        average_whatsapp_current = current_data[current_data["type"] == "WhatsApp"][
            "count"
        ].sum()
        average_leaddata_current = current_data[current_data["type"] == "LeadData"][
            "count"
        ].sum()
        average_inboundcall_current = current_data[
            current_data["type"] == "InboundCall"
        ]["count"].sum()

        current_data = pd.DataFrame(current_data)
        current_data["ChatDate"] = pd.to_datetime(current_data["ChatDate"]).dt.date
        current_data = (
            current_data.groupby(["ChatDate", "ProductName", "Status"])
            .sum()
            .reset_index()
        )
        current_totals = current_data.groupby("type")["count"].sum()

        if average_chat_current > average_chat_5_days:
            print("")
        elif average_sms_current > average_sms_5_days:
            print("")
        elif average_email_current > average_email_5_days:
            print("")
        elif average_ticket_current > average_ticket_5_days:
            print("")
        elif average_whatsapp_current > average_whatsapp_5_days:
            print("")
        elif average_leaddata_current > average_leaddata_5_days:
            print("")
        elif average_inboundcall_current > average_inboundcall_5_days:
            print("")

        result = {"data": data}
        # print(result)
        return result
    except Exception as ex:
        print(ex)
        return None
