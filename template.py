import os
from pathlib import Path
import logging

# Configure logging to display time-stamped messages
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "cnnClassifier"

# List of files and directories to be created in the project structure
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"


]



# Iterate through each file path in the list
for filepath in list_of_files:
    # Convert string paths to Path objects for better path handling
    filepath = Path(filepath)
    # Split the file path into directory (filedir) and filename
    filedir, filename = os.path.split(filepath)

# If the directory path (filedir) is not empty, create the directory
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")