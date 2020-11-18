import os
import boto3
from urllib.parse import urljoin


def get_extension(filename):
    return os.path.splitext(filename)[1]

def get_filename(filename):
    return os.path.split(filename)[1]


class S3Storage():

    def __init__(self, location, acl, app=None, **kwargs):
        self.acl = acl
        self.location = location
        self.custom_domain = custom_domain

        if app:
            self.init_app(app, **kwargs)
    

    def init_app(self, app, custom_domain=None):
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY']
        )
        self.bucket_name = app.config['AWS_STORAGE_BUCKET_NAME']
        self.custom_domain = custom_domain
        


    def save(self, fileobj, path):
        target = f"{self.location}/{path}"

        self.s3_client.upload_fileobj(
                fileobj,
                self.bucket_name,
                target,
                ExtraArgs={
                    "ACL": self.acl,
                    "ContentType": fileobj.content_type
                }
        )
        return self.url(path)

    
    def url(self, path):
        # if the file is public
        if self.custom_domain:
            url = urljoin(self.custom_domain, path)
            return url

        # if the file is private
        params = {}
        params['Bucket'] = self.bucket_name
        params['Key'] = f"{self.location}/{path}"
        url = self.s3_client.generate_presigned_url('get_object', Params=params, ExpiresIn=3600)

        return url
