import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO , format = '[%(asctime)s ] : %(message)s  :')
# logging.INFO -> indicating to display INFO in format

project_name = 'mlproject'

list_of_files = [
    f"src/{project_name}/__init.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init_.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init_.py",

    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb", # for notebook experiment
    "templates/index.html"

]



#python code to create folders and files 
for filepath in list_of_files: 
    filepath = Path(filepath)
    # handling issues related to / and \ 

    filedir , filename = os.path.split(filepath)
    # spliting between directory and file 

    # folder creating if not already exists
    if filedir != "":
        os.makedirs(filedir ,exist_ok=True)
        logging.info(f"Creating directory ; {filedir} for the file : {filename}")

    #file Creation 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):
        with open(filepath , "w") as f: # creating the new file 
            pass
            logging.info(f"Creating empty file : {filepath}")
    else :
        logging.info(f"{filename} is already exists ")