import boto3

logs = boto3.client("logs")

def read_log_group(group, limit=20):
    response = logs.describe_log_streams(
        logGroupName=group,
        orderBy="LastEventTime",
        descending=True,
        limit=1
    )

    if not response["logStreams"]:
        print("No hay streams.")
        return

    stream = response["logStreams"][0]["logStreamName"]

    events = logs.get_log_events(
        logGroupName=group,
        logStreamName=stream,
        limit=limit
    )

    for event in events["events"]:
        print(event["timestamp"], event["message"])


if __name__ == "__main__":
    read_log_group("/aws/lambda/mi-funcion")
