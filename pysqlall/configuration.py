
class Configuration(object):
    """
        Configuration object which stores information (database type, username,
        password) about each database
    """

    def __init__(self, defaultUsername = None, defaultPassword = None, defaultScript = None):
        self.defaultUsername = defaultUsername
        self.defaultPassword = defaultPassword
        self.defaultScript = defaultScript

