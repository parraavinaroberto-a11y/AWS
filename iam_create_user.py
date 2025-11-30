import boto3

iam = boto3.client("iam")

def create_user(username):
    print("Creando usuario:", username)
    response = iam.create_user(UserName=username)
    print("Usuario creado:", response["User"])


if __name__ == "__main__":
    create_user("usuario-demo")
