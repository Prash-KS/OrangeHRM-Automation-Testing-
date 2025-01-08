import configparser
import os

config = configparser.RawConfigParser()
config.read("../Configurations/config.ini")

# config_path = os.path.join(os.path.dirname(__file__), '../Configurations/config.ini')
# config.read(config_path)


class ReadConfig:
    @staticmethod
    def GetAplicationUrl():
        url = config.get("common info", "baseurl")
        return url

    @staticmethod
    def getusername():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def getpassword():
        password = config.get("common info", "password")
        return password

