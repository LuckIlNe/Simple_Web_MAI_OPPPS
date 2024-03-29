import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent
print(BASE_DIR)

config_path = BASE_DIR / 'config' / 'config.yaml'

def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config

config = get_config(config_path)
