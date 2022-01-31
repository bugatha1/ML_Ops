from src.utils.all_utils import read_config, create_directory, save_local_df
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split

def split_save_data(config_path, params_path):
    config = read_config(config_path)
    
    artifacts_dir = config["artifacts"]["artifacts_dir"]
    raw_local_dir = config["artifacts"]["raw_local_dir"]
    raw_local_file = config["artifacts"]["raw_local_file"]

    raw_local_file_path = os.path.join(artifacts_dir, raw_local_dir, raw_local_file)

    df = pd.read_csv(raw_local_file_path)

    params = read_config(params_path)

    test_size = params["base"]["test_size"]
    random_state = params["base"]["random_state"]

    train, test = train_test_split(df, test_size=test_size, random_state=random_state)

    split_data_dir = config["artifacts"]["split_data_dir"]
    create_directory([os.path.join(artifacts_dir, split_data_dir)])

    train_data_filename = config["artifacts"]["train"]
    test_data_filename = config["artifacts"]["test"]

    train_data_path = os.path.join(artifacts_dir, split_data_dir, train_data_filename)
    test_data_path = os.path.join(artifacts_dir, split_data_dir, test_data_filename)

    for data, data_path in (train, train_data_path), (test, test_data_path):
        save_local_df(data, data_path)

    print(df.head())


if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    split_save_data(parsed_args.config, parsed_args.params)