import click
import re


REGEXP = r"(s|S)3://(?P<bucket>.+?)/(?P<prefix>.+)"
S3URI_FORMAT = "https://s3.console.aws.amazon.com/s3/buckets/{bucket}?prefix={prefix}"


@click.command(context_settings={"ignore_unknown_options": True})
@click.argument("s3_uri")
def uri2url(s3_uri: str):
    """
    Convert S3 URI to URL
    """

    match = re.match(REGEXP, s3_uri)
    if not match:
        raise Exception(f"Invalid S3 URI: {s3_uri}")
    groupdict = match.groupdict()
    s3url = S3URI_FORMAT.format(**groupdict)
    print(s3url)
    return s3url
