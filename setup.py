from setuptools import setup, find_packages

setup(
    name="obfuscator",  # Your package name
    version="1.0.0",  # Version number
    author="Harry Jeffs",
    author_email="hjeffs30@gmail.com",
    description="General purpose obfuscation tool designed for GDPR obfuscation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hjeffs/Obfuscator",  # GitHub or website URL
    packages=["obfuscator"],
    install_requires=[
        # List dependencies here
        # pandas, boto3
        "pandas>=1.0.0",
        "boto3>=1.20.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Minimum Python version
)