import json
import yaml

with open("Hero.json", "r") as file:
    python_dict = json.load(file)

with open("Hero.yaml", "w") as file1:
    yaml.dump(python_dict, file1)

print("YAML file saved.")