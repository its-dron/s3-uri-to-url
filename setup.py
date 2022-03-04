from setuptools import setup

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='s3_uri_to_url',
    description='s3_uri_to_url - Convert S3 URI to URL',
    long_description=readme,
    long_description_content_type='text/markdown',
    version='0.1.2',
    author='Daniel Ron',
    author_email='dron@alum.mit.edu',
    url='https://github.com/its-dron/s3-uri-to-url',
    packages=['s3_uri_to_url'],
    install_requires=[
        'click'
    ],
    include_package_data=True,
    python_requires=">=3.6.*",
    license='Apache 2.0',
    zip_safe=False,
    entry_points={
        'console_scripts': ['s3-uri-to-url=s3_uri_to_url.main:uri2url'],
    }
)
