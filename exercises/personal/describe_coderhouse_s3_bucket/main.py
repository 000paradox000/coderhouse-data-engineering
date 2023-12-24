import boto3


def main():
    localstack_endpoint_url = 'http://s3:4566'
    s3 = boto3.client('s3', endpoint_url=localstack_endpoint_url)

    response = s3.list_buckets()

    print("S3 Buckets:")
    for bucket in response['Buckets']:
        print(f"- {bucket['Name']}")

        objects = s3.list_objects(Bucket=bucket['Name'])
        for obj in objects.get('Contents', []):
            print(f"    - {obj['Key']}")


if __name__ == "__main__":
    main()
