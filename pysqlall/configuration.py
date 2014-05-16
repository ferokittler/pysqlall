# Config file example
# database_type;username;password;connection_string:script
# oracle;hr;hr;hrdb.example.com;script;


class configuration(object):
    """
        Configuration object which stores information (database type, username,
        password) about each database
    """

    def __init__(self):
        pass

    def parseConfiguration(self, filename):
        """
            Parse configuration file (or configuration passed on command line?)
            to fill configuration object with values
        """
        handle = open(filename)
        close(handle)

    def isPrepared(self):
        """
            Method checks if all requred information are filled
        """

        pass

