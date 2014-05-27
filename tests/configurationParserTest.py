import unittest
from pysqlall import configurationParser

class TestConfigurationParser(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

        
    def testCreationOfConfigurationParserWithEmptyConfiguration(self):
        #self.cp = configurationParser.ConfigurationParser()
        self.assertRaisesRegexp(ValueError, "Configuration is empty!", configurationParser.ConfigurationParser, "")

    def testCreationOfConfigurationParserWithWhitespaceConfiguration(self):
        #self.cp = configurationParser.ConfigurationParser()
        self.assertRaisesRegexp(ValueError, "Configuration is empty!", configurationParser.ConfigurationParser, " \n  \t  ")

    def testCreationOfConfigurationParserWithInlineConfiguration(self):
        self.cp = configurationParser.ConfigurationParser("oracle;hr;hr;hrdb.example.com;script;")
        self.assertEquals(self.cp.configuration, "oracle;hr;hr;hrdb.example.com;script;")

    def testFileConfigurationType(self):
        self.cp = configurationParser.ConfigurationParser("@/tmp/nonexistent.sql")
        self.assertEquals(self.cp.configurationType, self.cp.FILE)

    def testInlineConfigurationType(self):
        self.cp = configurationParser.ConfigurationParser("oracle;hr;hr;hrdb.example.com;script;")
        self.assertEquals(self.cp.configurationType, self.cp.INLINE)

    def testParseInlineConfigurationWith6semicolons(self):
        self.cp = configurationParser.ConfigurationParser("oracle;hr;hr;hrdb.example.com;script;;")
        self.assertRaisesRegexp(ValueError, "Configuration on line 1 has incorrect format - too many semicolons", self.cp.parse)

    def testParseInlineConfigurationWith5semicolons(self):
        self.cp = configurationParser.ConfigurationParser("oracle;hr;hr;hrdb.example.com;script")
        self.assertRaisesRegexp(ValueError, "Configuration on line 1 has incorrect format - too few semicolons", self.cp.parse)

    def testParseInlineConfigurationWith5semicolonsOnSecondLine(self):
        self.cp = configurationParser.ConfigurationParser("oracle;hr;hr;hrdb.example.com;script;\noracle;hr;hr;hrdb2.example.com;script")
        self.assertRaisesRegexp(ValueError, "Configuration on line 2 has incorrect format - too few semicolons", self.cp.parse)

    def testFileConfigurationWhenFileDoesNotExists(self):
        self.cp = configurationParser.ConfigurationParser("@/tmp/nonexistent.sql")
        self.assertRaisesRegexp(ValueError, "Configuration file /tmp/nonexistent.sql does not exists!", self.cp.parse)
        



suite = unittest.TestLoader().loadTestsFromTestCase(TestConfigurationParser)
unittest.TextTestRunner(verbosity=2).run(suite)

