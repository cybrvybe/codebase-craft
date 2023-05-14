# convert_to_yaml.py
import json
import yaml
import sys


def convert_to_yaml(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)
    return yaml.dump(data)


if __name__ == "__main__":
    json_file = sys.argv[1]
    print(convert_to_yaml(json_file))
