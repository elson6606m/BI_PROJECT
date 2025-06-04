from prefect import flow, task
import subprocess
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

@task
def extract():
    subprocess.run(["python", "extract.py"], check=True)

@task
def load():
    subprocess.run(["python", "load.py"], check=True)

@task
def transform():
    subprocess.run(["dbt", "run"], cwd="dbt", check=True)

@flow
def stock_pipeline():
    extract()
    load()
    transform()

if __name__ == "__main__":
    stock_pipeline()
