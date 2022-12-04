import os
import sqlite3
import configparser
import sys
import binascii
from colorama import Fore

def setup() -> None:
    supported_langs = ["DE"]
    config = configparser.ConfigParser()
    config.read("app_config.ini")
    path = os.path.abspath(os.path.dirname(__file__))
    if str(config['GENERAL']['app_path'].replace(" ", "")).strip() == "":
        # Putting application path in the config
        config['GENERAL']['app_path'] = path
    # Generating a 128 char long string and storing it in the config
    print(Fore.WHITE + "Generating Flask secret... ", file=sys.stdout, end="")
    config['GENERAL']['flask_secret'] = str(binascii.b2a_hex(os.urandom(128)).decode())
    print(Fore.GREEN + "Done" + Fore.RESET, file=sys.stdout)
    if not config['GENERAL']['locale'] in supported_langs:
        print(Fore.RED + f'[ERR] locale "{ config["GENERAL"]["locale"] }" is not valid or has not been implemented yet... Exiting!' + Fore.RESET, file=sys.stderr)
        exit(-1)
    # Writing the config
    config.write(open('app_config.ini', 'w'))
    # Initializing the Database
    try:
        # Creating a folder to hold all Databases in
        os.makedirs(config['GENERAL']['app_path']+"/databases")
        # Creating a new Database for admin panel logins
        print(Fore.WHITE + "Creating login database and table... ", file=sys.stdout, end="")
        con = sqlite3.connect(config['GENERAL']['app_path']+"/databases/user_accounts.db")
        cur = con.cursor()
        # Creating the Table
        cur.execute("CREATE TABLE users(email, password)")
        # Commiting the Database
        con.commit()
        con.close()
        print(Fore.GREEN + "Done\nSetup finished" + Fore.RESET, file=sys.stdout)
    except Exception:
        print(Fore.RED + "Failed to create the Database!" + Fore.RESET, file=sys.stderr)
        exit(-1)