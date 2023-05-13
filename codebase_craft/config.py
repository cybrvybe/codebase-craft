import yaml

def load_config():
    with open(r'C:\Users\alexf\software-projects\codebase-craft\codebase_craft\config\app_config.yaml', 'r') as f:
        return yaml.safe_load(f)

config = load_config()

SCRIPT_DIR = config['script_dir']
OPENAI_API_KEY = config['openai_api_key']
