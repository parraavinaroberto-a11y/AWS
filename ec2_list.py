import boto3

ec2 = boto3.client("ec2")

def list_instances():
    response = ec2.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print("ID:", instance["InstanceId"])
            print("Tipo:", instance["InstanceType"])
            print("Estado:", instance["State"]["Name"])
            print("AZ:", instance["Placement"]["AvailabilityZone"])
            print("-" * 30)

if __name__ == "__main__":
    list_instances()
