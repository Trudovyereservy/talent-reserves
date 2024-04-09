from storages.backends.s3boto3 import S3Boto3Storage

from .settings import (YANDEX_BUCKET_NAME,
                       YANDEX_PUBLIC_MEDIA_LOCATION)


class ClientDocsStorage(S3Boto3Storage):
    bucket_name = YANDEX_BUCKET_NAME
    custom_domain = "storage.yandexcloud.net"
    secure_urls = True


class ClientMediaStorage(S3Boto3Storage):
    bucket_name = YANDEX_BUCKET_NAME
    location = YANDEX_PUBLIC_MEDIA_LOCATION
    file_overwrite = False
    secure_urls = True
