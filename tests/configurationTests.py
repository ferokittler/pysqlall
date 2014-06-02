import unittest
from pysqlall import configuration
from pysqlall import configurationParser
from pysqlall import database

class TestConfiguration(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def testCreationOfConfigurationWithEmptyConfigurationString(self):
        self.assertRaisesRegexp(ValueError, "Configuration string is empty!", configuration.Configuration, "")

    def testCreationOfConfigurationWithWhitespaceConfigurationString(self):
        self.assertRaisesRegexp(ValueError, "Configuration string is empty!", configuration.Configuration, " \n  \t  ")


    def testEmptyDatabasesAfterCreation(self):
        self.c = configuration.Configuration(configurationString = "randomString")
        self.assertListEqual(self.c.databases, [])

    def testDefaultUsername(self):
        self.c = configuration.Configuration(configurationString = "randomString", defaultUsername = "defaultOraUser")
        self.assertEquals(self.c.defaultUsername, "defaultOraUser")
        
    def testDefaultUsernameIsNone(self):
        self.c = configuration.Configuration(configurationString = "randomString")
        self.assertIsNone(self.c.defaultUsername)

    def testDefaultPassword(self):
        self.c = configuration.Configuration(configurationString = "randomString", defaultPassword = "defaultOraPassword")
        self.assertEquals(self.c.defaultPassword, "defaultOraPassword")
        
    def testDefaultPasswordIsNone(self):
        self.c = configuration.Configuration(configurationString = "randomString")
        self.assertIsNone(self.c.defaultPassword)

    def testDefaultScript(self):
        self.c = configuration.Configuration(configurationString = "randomString", defaultScript = "defaultOraScript")
        self.assertEquals(self.c.defaultScript, "defaultOraScript")
        
    def testDefaultScriptIsNone(self):
        self.c = configuration.Configuration(configurationString = "randomString")
        self.assertIsNone(self.c.defaultScript)

    def testAllDefaultValues(self):
        self.c = configuration.Configuration("contentOfConfigurationString", "defaultOraUser", "defaultOraPassword", "defaultOraScript")
        self.assertEquals(self.c.defaultUsername, "defaultOraUser")
        self.assertEquals(self.c.defaultPassword, "defaultOraPassword")
        self.assertEquals(self.c.defaultScript, "defaultOraScript")
        self.assertEquals(self.c.configurationString, "contentOfConfigurationString")

    def testIfConfigurationParserIsCreatedInInit(self):
        self.c = configuration.Configuration(configurationString = "randomString")
        self.assertIsNotNone(self.c.configurationParser)
        self.assertIsInstance(self.c.configurationParser, configurationParser.ConfigurationParser)

class TestConfigurationReadMethod(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSingleLineConfiguration(self):
        self.c = configuration.Configuration("oracle;oraUser;oraPwd;connectionString;script")
        self.c.read()
        self.assertListEqual(self.c.databases, [database.Database("oracle", "oraUser", "oraPwd", "connectionString", "script")])

    def testSingleLineConfigurationWithoutUsername(self):
        self.c = configuration.Configuration("oracle;;oraPwd;connectionString;script", defaultUsername = "defaultOracleUsername")
        self.c.read()
        self.assertListEqual(self.c.databases, [database.Database("oracle", "defaultOracleUsername", "oraPwd", "connectionString", "script")])

    def testSingleLineConfigurationWithoutUsernameAndDefaultUsernameIsNotSet(self):
        self.c = configuration.Configuration("oracle;;oraPwd;connectionString;script")
        self.assertRaisesRegexp(ValueError, "Missing [^ ]* and no default value for [^ ]* is set!", self.c.read)

    def testSingleLineConfigurationWithoutPassword(self):
        self.c = configuration.Configuration("oracle;oraUser;;connectionString;script", defaultPassword = "defaultOraclePassword")
        self.c.read()
        self.assertListEqual(self.c.databases, [database.Database("oracle", "oraUser", "defaultOraclePassword", "connectionString", "script")])

    def testSingleLineConfigurationWithoutPasswordAndDefaultPasswordIsNotSet(self):
        self.c = configuration.Configuration("oracle;oraUser;;connectionString;script")
        self.assertRaisesRegexp(ValueError, "Missing [^ ]* and no default value for [^ ]* is set!", self.c.read)

    def testSingleLineConfigurationWithoutScript(self):
        self.c = configuration.Configuration("oracle;oraUser;oraPwd;connectionString;", defaultScript = "defaultScript")
        self.c.read()
        self.assertListEqual(self.c.databases, [database.Database("oracle", "oraUser", "oraPwd", "connectionString", "defaultScript")])

    def testSingleLineConfigurationWithoutScriptAndDefaultScriptIsNotSet(self):
        self.c = configuration.Configuration("oracle;oraUser;oraPwd;connectionString;")
        self.assertRaisesRegexp(ValueError, "Missing [^ ]* and no default value for [^ ]* is set!", self.c.read)

    def testSingleLineConfigurationWithoutUsernamePasswordAndScript(self):
        self.c = configuration.Configuration("oracle;;;connectionString;", defaultUsername = "defaultOraUser",
                                                                           defaultPassword = "defaultOraPassword",
                                                                           defaultScript = "defaultScript")
        self.c.read()
        self.assertListEqual(self.c.databases, [database.Database("oracle", "defaultOraUser", "defaultOraPassword", "connectionString", "defaultScript")])

    def testMultiLineConfigurationWithoutUsernamePasswordAndScript(self):
        self.c = configuration.Configuration("oracle;;;connectionString;\n oracle;user1;pwd1;connectionString2;",
                                                                           defaultUsername = "defaultOraUser",
                                                                           defaultPassword = "defaultOraPassword",
                                                                           defaultScript = "defaultScript")
        self.c.read()
        self.d1 = database.Database("oracle", "defaultOraUser", "defaultOraPassword", "connectionString", "defaultScript")
        self.d2 = database.Database("oracle", "user1", "pwd1", "connectionString2", "defaultScript")
        self.assertListEqual(self.c.databases, [self.d1, self.d2])


suite = unittest.TestLoader().loadTestsFromTestCase(TestConfiguration)
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestConfigurationReadMethod))
unittest.TextTestRunner(verbosity=2).run(suite)

