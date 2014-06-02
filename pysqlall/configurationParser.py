# Config file example
# database_type;username;password;connection_string:script
# oracle;hr;hr;hrdb.example.com;script;

#from pysqlall import database
import database


class ConfigurationParser(object):
    """
        ConfigurationParser is responsible for creating corresponding database objects from given configuration (file or string)
    """

    FILE = 1
    INLINE = 2

    def __init__(self, configuration = ""):
    
        self.configuration = configuration

        if configuration[0] == '@':
            self.configurationType = self.FILE
        else:
            self.configurationType = self.INLINE

    def parse(self):
        
        databases = []

        if self.configurationType == self.INLINE:
            databases = self.doParsing(self.configuration.split('\n'))

        if self.configurationType == self.FILE:
            try:
                handle = open(self.configuration[1:])
                databases = self.doParsing(handle.readlines()) 
                handle.close()
            except IOError:
                raise ValueError('Configuration file %s does not exists!' % self.configuration[1:])
            
        return databases
            


    def doParsing(self, configurationContent):
        """
            Parse configuration file (or configuration passed on command line?)
            to fill configuration object with values
        """
        
        databases = []

        #lines = self.configurationContent.split('\n')
        i = 1
        for line in configurationContent:
            line = line.strip()
            if line.count(';') > 4:
                raise ValueError("Configuration on line %d has incorrect format - too many semicolons!" % i)

            if line.count(';') < 4:
                raise ValueError("Configuration on line %d has incorrect format - too few semicolons!" % i)

            type, username, password, connection, script = line.split(';')
            databases.append(database.Database(type, username, password, connection, script))
            i+=1

        return databases
            

