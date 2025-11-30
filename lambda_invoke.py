import boto3
import json

lambda_client = boto3.client("lambda")

def invoke_lambda(function_name, payload):
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType="RequestResponse",
        Payload=json.dumps(payload)
    )
    res_payload = response["Payload"].read().decode("utf-8")
    print("Respuesta de Lambda:", res_payload)


if __name__ == "__main__":
    invoke_lambda(
        "mi-funcion-lambda",
        {"mensaje": "Hola desde Python"}
    )
