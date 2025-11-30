import boto3

s3 = boto3.client("s3")

def upload_file(bucket, local_path, key):
    s3.upload_file(local_path, bucket, key)
    print(f"Archivo subido: {local_path} → s3://{bucket}/{key}")


def download_file(bucket, key, local_path):
    s3.download_file(bucket, key, local_path)
    print(f"Archivo descargado: s3://{bucket}/{key} → {local_path}")


if __name__ == "__main__":
    BUCKET = "tu-bucket"
    upload_file(BUCKET, "archivo.txt", "carpeta/archivo.txt")
    download_file(BUCKET, "carpeta/archivo.txt", "descarga.txt")
