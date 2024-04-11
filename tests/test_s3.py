import boto3
import botocore

from talent_reserves.settings import (AWS_ACCESS_KEY_ID,
                                      AWS_SECRET_ACCESS_KEY,
                                      YANDEX_CLOUD_DOMAIN,
                                      YANDEX_BUCKET_NAME)


def test_connection_s3():
    session = boto3.session.Session()
    s3 = session.resource(
        service_name='s3',
        endpoint_url=f'https://{YANDEX_CLOUD_DOMAIN}',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    try:
        s3.meta.client.head_bucket(Bucket=YANDEX_BUCKET_NAME)
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        # 403 - нет доступа/ 404 - не существует
        assert error_code == 404, 'Отсутствует доступ к bucket'
