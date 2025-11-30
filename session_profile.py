import boto3

def get_session(profile="default", region="us-east-1"):
    return boto3.Session(profile_name=profile, region_name=region)


if __name__ == "__main__":
    session = get_session("dev")
    s3 = session.client("s3")
    print("Buckets:", s3.list_buckets()["Buckets"])
