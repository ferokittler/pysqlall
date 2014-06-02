import configurationParser

class Configuration(object):
    """
        Configuration object which stores information (database type, username,
        password) about each database
    """

    def __init__(self, configurationString, defaultUsername = None, defaultPassword = None, defaultScript = None):

        if configurationString.strip() == "":
            raise ValueError("Configuration string is empty!")

        self.configurationString = configurationString
        self.defaultUsername = defaultUsername
        self.defaultPassword = defaultPassword
        self.defaultScript = defaultScript

        self.configurationParser = configurationParser.ConfigurationParser(configurationString)

        self.databases = []

    def read(self):
        self.databases = self.configurationParser.parse()

        for database in self.databases:
            if database.username == "":
                if self.defaultUsername == None:
                    raise ValueError("Missing %s and no default value for %s is set!" % ("username", "username"))
                database.username = self.defaultUsername

            if database.password == "":
                if self.defaultPassword == None:
                    raise ValueError("Missing %s and no default value for %s is set!" % ("password", "password"))
                database.password = self.defaultPassword

            if database.script == "":
                if self.defaultScript == None:
                    raise ValueError("Missing %s and no default value for %s is set!" % ("script", "script"))
                database.script = self.defaultScript


