# S3 URI to URL

Command line tool that converts S3 URIs to a valid aws console URL.

Assumes you are already logged into the appropriate account - this tool does not handle credentials or sessions at all.

## Usage

```
$ s3-uri-to-url s3://sample_bucket/any/long/prefix-string/
https://s3.console.aws.amazon.com/s3/buckets/sample_bucket?prefix=any/long/prefix-string/
```


## Installation

```
pip install s3_uri_to_url
```