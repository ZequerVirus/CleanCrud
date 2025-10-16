from setuptools import setup, find_packages

setup(
    name="crudcleanarch",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=5.2, <6.0",
    ],
    author="ZequerVirus",
    description="Generador de código con arquitectura limpia para Django",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ZequerVirus/CleanCrud",
    # packages=find_packages(),
    # include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Framework :: Django :: 5.2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
    license="MIT",
)
