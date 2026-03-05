from setuptools import setup, find_packages

setup(
    name="cloudera-manager-sdk",
    version="0.1.0",
    description="SDK Python completo per Cloudera Manager CDP",
    author="Tu Nome",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0"
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "cm-sdk = cm_sdk.cli:main"
        ]
    }
)