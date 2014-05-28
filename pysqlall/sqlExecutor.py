import database

class SqlExecutor(object):
    """
        Abstract object responsible for executing sql command or script on single database
    """

    def __init__(self, database):
        self.database = database    
        self.returnCode = None
        self.returnMessage = None

    def execute(self):
        pass

    
