import unittest
from pysqlall import configuration

class TestConfiguration(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDefaultUsername(self):
        self.c = configuration.Configuration(defaultUsername = "defaultOraUser")
        self.assertEquals(self.c.defaultUsername, "defaultOraUser")
        
    def testDefaultUsernameIsNone(self):
        self.c = configuration.Configuration()
        self.assertIsNone(self.c.defaultUsername)

    def testDefaultPassword(self):
        self.c = configuration.Configuration(defaultPassword = "defaultOraPassword")
        self.assertEquals(self.c.defaultPassword, "defaultOraPassword")
        
    def testDefaultPasswordIsNone(self):
        self.c = configuration.Configuration()
        self.assertIsNone(self.c.defaultPassword)

    def testDefaultScript(self):
        self.c = configuration.Configuration(defaultScript = "defaultOraScript")
        self.assertEquals(self.c.defaultScript, "defaultOraScript")
        
    def testDefaultScriptIsNone(self):
        self.c = configuration.Configuration()
        self.assertIsNone(self.c.defaultScript)

    def testAllDefaultValues(self):
        self.c = configuration.Configuration("defaultOraUser", "defaultOraPassword", "defaultOraScript")
        self.assertEquals(self.c.defaultUsername, "defaultOraUser")
        self.assertEquals(self.c.defaultPassword, "defaultOraPassword")
        self.assertEquals(self.c.defaultScript, "defaultOraScript")


suite = unittest.TestLoader().loadTestsFromTestCase(TestConfiguration)
unittest.TextTestRunner(verbosity=2).run(suite)

