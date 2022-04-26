#!/usr/bin/env python3

import os
import ruamel.yaml as yaml
from mergedeep import merge


def convert_properties_to_yaml(config_dict):
    yaml_dict = {}
    for key, value in config_dict.items():
        config_keys = key.split(".")
        for config_key in reversed(config_keys):
            value = {config_key: value}
        yaml_dict = merge(yaml_dict, value)
    return yaml_dict


def read_yaml_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def merge_yaml_files(file_paths):
    result = {}
    for file_path in file_paths:
        result.update(read_yaml_file(file_path))
    return convert_properties_to_yaml(result)


def dump_file(filePath, data):
    with open(filePath, "w") as f:
        yaml.dump(data, f, default_flow_style=False)


def get_files_from_dir(dirPath):
    return [os.path.join(dirPath, f)
            for f in os.listdir(dirPath)
            if os.path.isfile(os.path.join(dirPath, f))]


def main():
    filePaths = get_files_from_dir('config')
    res = merge_yaml_files(filePaths)
    dump_file("merged.yaml", res)


if __name__ == '__main__':
    main()
