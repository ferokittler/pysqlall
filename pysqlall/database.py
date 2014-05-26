
class Database(object):
    def __init__(self, type, username, password, connection, script):
        self.type = type
        self.username = username
        self.password = password
        self.connection = connection
        self.script = script

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

