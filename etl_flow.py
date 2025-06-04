from prefect import flow, task
import subprocess

@task
def extract():
    print("📤 Running extract.py...")
    subprocess.run(["python", "extract.py"], check=True)

@task
def load():
    print("📦 Running load.py...")
    subprocess.run(["python", "load.py"], check=True)

@task
def transform():
    print("🔄 Running dbt models...")
    subprocess.run(["dbt", "run"], cwd="dbt/my_dbt_project", check=True)

@flow(name="Stock Market ETL")
def etl_pipeline():
    extract()
    load()
    transform()

if __name__ == "__main__":
    etl_pipeline()
