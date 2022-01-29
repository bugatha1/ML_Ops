from setuptools import setup

with open('README.md', 'r', encoding= 'utf-8') as f:
    long_description = f.read()

setup(
    name="src",
    version = "0.0.1",
    author = "bugatha1",
    description = "AI ML Ops package",
    Long_description = long_description,
    Long_description_content_type = "text/markdown",
    url="https://github.com/bugatha1/ML_Ops.git",
    author_name="bugatha1",
    packages=["src"],
    python_requires = ">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ] 
)