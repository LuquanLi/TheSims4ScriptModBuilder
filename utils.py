import os
from pathlib import Path
import shutil
import string


def create_directory(path: string):
    Path(path).mkdir(parents=True, exist_ok=True)


# remove all files in this directory
def clean_directory(path: string):
    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)


def prepare_directory(path: string):
    clean_directory(path)
    create_directory(path)

