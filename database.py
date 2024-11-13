# # database.py
# from pymongo import MongoClient


# def getCollection(collection_name):
#     client = MongoClient(
#         'mongodb://LoggerUser:##LoggerDBPass##@10.25.4.25:27017/?authSource=LoggerDB&authMechanism=SCRAM-SHA-1&directConnection=true'
#     )
#     db = client["YourDatabaseName"]
#     collection = db[collection_name]
#     return collection

# database.py


def getCollection(collection_name):
    # Sample demo data for testing
    demo_data = [
        {
            "type": "Chat",
            "startTime": "2024-11-07T08:00:00",
            "data": [
                {
                    "ChatDate": "2024-11-07",
                    "ProductName": "Product1",
                    "Status": "Completed",
                    "count": 10,
                }
            ],
        },
        {
            "type": "SMS",
            "startTime": "2024-11-08T08:00:00",
            "data": [
                {
                    "ChatDate": "2024-11-08",
                    "ProductName": "Product2",
                    "Status": "Pending",
                    "count": 15,
                }
            ],
        },
        {
            "type": "Email",
            "startTime": "2024-11-09T08:00:00",
            "data": [
                {
                    "ChatDate": "2024-11-09",
                    "ProductName": "Product3",
                    "Status": "Completed",
                    "count": 8,
                }
            ],
        },
        {
            "type": "Ticket",
            "startTime": "2024-11-10T08:00:00",
            "data": [
                {
                    "ChatDate": "2024-11-10",
                    "ProductName": "Product4",
                    "Status": "Completed",
                    "count": 5,
                }
            ],
        },
    ]

    # Simulating data retrieval based on collection_name
    if collection_name == "CommData":
        # Flattening the data by extracting necessary attributes
        flattened_data = []
        for record in demo_data:
            for entry in record["data"]:
                # Add additional fields from the parent record (e.g., type, startTime)
                flattened_entry = entry.copy()
                flattened_entry["type"] = record["type"]
                flattened_entry["startTime"] = record["startTime"]
                flattened_data.append(flattened_entry)

        return flattened_data
    else:
        return []
