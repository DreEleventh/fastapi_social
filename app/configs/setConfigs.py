import configparser


def set_db_config():
    config_obj = configparser.ConfigParser()
    config_obj.read("AppConfigFile.ini")
    dbconfig = config_obj['dbConnect']['sqlalchemy_database_url']

    return dbconfig


def set_secret_key():
    config_obj = configparser.ConfigParser()
    config_obj.read("AppConfigFile.ini")
    secret_key = config_obj['auth']

    return secret_key["secret_key"]
