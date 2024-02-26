# # default code to keep inside setup.py

# import setuptools

# with open("README.md" , "r" , encoding = "utf-8") as f:
#     long_description = f.read()

# __version__ = "0.0.0"

# REPO_NAME = "End-to-End-ML-Project-Implementation"
# AUTHOR_USER_NAME = "animeshkr7"
# SRC_REPO = "mlproject" # inside src the name provided
# AUTHOR_EMAIL = "animeshkr7@gmail.com"

# #setup src/mlproject as local package 
# setuptools.setup(
#     name = SRC_REPO,
#     version=__version__,
#     author=AUTHOR_USER_NAME,
#     author=AUTHOR_EMAIL,
#     description= "A small python package for ml app",
#     long_description= long_description,
#     url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/",
#     project_urls = {
#         "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
#     },
#     package_dir={"": "src"},
#     packages=setuptools.find_packages(where="src"),

# )

# # setup.py will automatically figure out __init__ contructor in each and every folder , thus enablabling it as local package
  

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-end-ML-Project-Implementation"
AUTHOR_USER_NAME = "animeshkr7"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "animeshkr7@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)


# as main.py is outside the src folder , so to access src methods we create setup.py 
# for making src as local package  inside the environment