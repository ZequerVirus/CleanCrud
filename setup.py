from setuptools import setup, find_packages

setup(
    name="django-cleancodegen",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=3.2",
    ],
    author="ZequerVirus",
    description="Generador de código con arquitectura limpia para Django",
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
    ],
)
