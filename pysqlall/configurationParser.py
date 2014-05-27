# Config file example
# database_type;username;password;connection_string:script
# oracle;hr;hr;hrdb.example.com;script;


class ConfigurationParser(object):
    """
        ConfigurationParser is responsible for creating corresponding database objects from given configuration (file or string)
    """

    FILE = 1
    INLINE = 2

    def __init__(self, configuration = ""):

        if configuration.strip() == "":
            raise ValueError("Configuration is empty!")

        self.configuration = configuration

        if configuration[0] == '@':
            self.configurationType = self.FILE
        else:
            self.configurationType = self.INLINE

    def parse(self):
        if self.configurationType == self.INLINE:
            self.doParsing()

        if self.configurationType == self.FILE:
            try:
                handle = open(self.configuration[1:])
                close(handle)
            except IOError:
                raise ValueError('Configuration file %s does not exists!' % self.configuration[1:])
            
            


    def doParsing(self):
        """
            Parse configuration file (or configuration passed on command line?)
            to fill configuration object with values
        """
        
        lines = self.configuration.split('\n')
        i = 1
        for line in lines:
            if line.count(';') > 5:
                raise ValueError("Configuration on line %d has incorrect format - too many semicolons!" % i)

            if line.count(';') < 5:
                raise ValueError("Configuration on line %d has incorrect format - too few semicolons!" % i)
            i+=1
            
