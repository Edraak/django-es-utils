from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="django_es_utils",
    version="0.0.6",
    url="https://github.com/Edraak/django-es-utils",
    description="Elasticsearch utilities for Django projects.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Fahmi Al-Najjar",
    author_email="fahmi.najjar@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "Django>=5.2.4",
        "requests",
        "urllib3>=2.5.0",
        "elasticsearch==8.18.1",
        "elasticsearch_dsl==8.18.0",
        "ElasticMock==1.8.1"
    ],
)
