import os
from invoke import task

@task
def startdev(c):
    c.run("poetry config virtualenvs.in-project true --local")
    c.run("poetry install")
    download_data(c)

@task
def download_data(c):
    os.makedirs("data", exist_ok=True)
    with c.cd("data"):
        if not os.path.exists("data/HIGGS.csv"):
            c.run("wget https://archive.ics.uci.edu/ml/machine-learning-databases/00280/HIGGS.csv.gz")
            c.run("gunzip HIGGS.csv.gz")

@task
def run(c, arg):
    c.run("poetry run python3.12 src/{arg}")