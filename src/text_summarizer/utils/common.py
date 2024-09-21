import os
from box.exceptions import BoxValueError
import yaml 
from text_summarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any 

@ensure_annotations() #this decorator is to avoid wrong data type input to the functions below
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml, 'r') as file:
            config = yaml.safe_load(file)
        return ConfigBox(config)
    except BoxValueError as e:
        logger.error(f"Error reading YAML file: {e}")
        raise e
    except Exception as e:
        logger.error(f"An unexpected error occurred while reading YAML file: {e}")
        raise e

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Directory '{path}' created.")

@ensure_annotations
def get_size(path:Path)-> str:
    size = round(os.path.getsize(path)/1024)
    return f"{size} kilobytes"
