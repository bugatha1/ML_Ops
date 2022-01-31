import yaml
import os

def read_config(path_to_file: str) -> dict:
    with open(path_to_file) as yaml_file:
        content = yaml.safe_load(yaml_file)
        
    return content

def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"directory is create at {dir_path}")

def save_local_df(data, data_path, index_state=False):
    data.to_csv(data_path, index=index_state)
    print(f"data is save at {data_path}")

