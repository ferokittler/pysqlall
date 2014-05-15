
# TODO: object design

# Config file example
# database_type;username;password;connection_string:script
# oracle;hr;hr;hrdb.example.com;script;

class database(object):
    """
        Object representing single database with its properties
    """

    def __init__(self, type, username, password, conn, script):
        self.type = type
        self.username = username
        self.password = password
        self.conn = conn
        self.script = script

class configuration(object):
    """
        Configuration object which stores information (database type, username,
        password) about each database
    """

    def __init__(self):
        pass

    def parseConfigration(self, filename):
        """
            Parse configuration file (or configuration passed on command line?)
            to fill configuration object with values
        """
        pass

    def isPrepared(self):
        """
            Method checks if all requred information are filled
        """

        pass


import argparse
parser = argparse.ArgumentParser(description = "Tool for running SQL code on multiple databases")
parser.add_argument("-u", "--username", help="username for connecting to database")
parser.add_argument("-p", "--password", help="password for connecting to database")
parser.add_argument("-d", "--database", help="connection string for database")
parser.add_argument("-s", "--script", help="file containing SQL code")
args = parser.parse_args()

print "Here comes the sun..."
