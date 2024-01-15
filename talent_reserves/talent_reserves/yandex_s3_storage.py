from storages.backends.s3boto3 import S3Boto3Storage

from .settings import YANDEX_CLIENT_DOCS_BUCKET_NAME


class ClientDocsStorage(S3Boto3Storage):
    bucket_name = YANDEX_CLIENT_DOCS_BUCKET_NAME
    file_overwrite = False
