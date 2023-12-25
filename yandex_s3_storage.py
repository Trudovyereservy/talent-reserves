from sites.crm.settings import BUCKET_NAME
from storages.backends.s3boto3 import S3Boto3Storage


class ClientDocsStorage(S3Boto3Storage):
    bucket_name = BUCKET_NAME
    file_overwrite = False
