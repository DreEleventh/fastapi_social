import configparser

config = configparser.ConfigParser()

config['dbConnect'] = {'sqlalchemy_database_url': 'postgresql://postgres:ZamBase089@localhost/fastapi'}


config["auth"] = {"secret_key": "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"}


with open(r'AppConfigFile.ini', 'w') as configFile:
    config.write(configFile)
