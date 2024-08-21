from setuptools import setup, find_packages

setup(
    name="trackerpy",
    version="0.2",
    packages=find_packages(),
    description="A logging utility for Python Scripts",
    author="Matheus Rodrigo Kanczewski Bressan",
    author_email="matheus.bressan20@gmail.com",
    install_requires=[
        'pyodbc'
    ]
)