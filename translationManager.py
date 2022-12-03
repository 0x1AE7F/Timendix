import configparser
import json

def init_translator() -> json:
    # Creating a new ConfigParser instance
    config = configparser.ConfigParser()
    # Reading from the config file
    config.read("app_config.ini")
    # Opening the correct translations json file
    with open(f"{config['GENERAL']['app_path']}/lang/{config['GENERAL']['locale']}.json") as f:
        # Loading the translations
        json_data = json.load(f)
        f.close()
        return json_data