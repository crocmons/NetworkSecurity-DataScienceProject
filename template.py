import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_path = "networksecurity"

list_of_files = [
    ".github/workflows/main.yaml",
    "Network_Data/data.csv",
    f"{project_path}/__init__.py",
    f"{project_path}/components/__init__.py",
    f"{project_path}/utils/__init__.py",
    f"{project_path}/utils/common.py",
    f"{project_path}/cloud/__init__.py",
    f"{project_path}/exception/__init__.py",
    f"{project_path}/logging/__init__.py",
    f"{project_path}/config/__init__.py",
    f"{project_path}/pipeline/__init__.py",
    f"{project_path}/entity/__init__.py",
    f"{project_path}/entity/config_entity.py",
    f"{project_path}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "DockerFile",
    "setup.py",
    "notebooks/research.ipynb",
    "templates/index.html",
    "app.py",
    ".env",
    "requirements.txt",
    ".gitignore",
    "README.md",


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty files: {filepath}")

    else:
        logging.info(f"{filename} is already exists!")            
