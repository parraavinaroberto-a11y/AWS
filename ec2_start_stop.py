import boto3

ec2 = boto3.client("ec2")

def start_instance(instance_id):
    print("Iniciando instancia:", instance_id)
    ec2.start_instances(InstanceIds=[instance_id])


def stop_instance(instance_id):
    print("Deteniendo instancia:", instance_id)
    ec2.stop_instances(InstanceIds=[instance_id])


if __name__ == "__main__":
    # Cambia por tu instancia
    INSTANCE = "i-0123456789abcdef0"

    start_instance(INSTANCE)
    # stop_instance(INSTANCE)
