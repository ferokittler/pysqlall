import unittest
from pysqlall import configurationParser
from pysqlall import database
import os

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
        self.cp = configurationParser.ConfigurationParser("oracle;hr;hr;hrdb.example.com;script")
        self.assertEquals(self.cp.configuration, "oracle;hr;hr;hrdb.example.com;script")

    def testFileConfigurationType(self):
        self.cp = configurationParser.ConfigurationParser("@/tmp/nonexistent.sql")
        self.assertEquals(self.cp.configurationType, self.cp.FILE)

    def testInlineConfigurationType(self):
        self.cp = configurationParser.ConfigurationParser("oracle;hr;hr;hrdb.example.com;script")
        self.assertEquals(self.cp.configurationType, self.cp.INLINE)

    def testParseInlineConfigurationWith5semicolons(self):
        self.cp = configurationParser.ConfigurationParser("oracle;hr;hr;hrdb.example.com;script;")
        self.assertRaisesRegexp(ValueError, "Configuration on line 1 has incorrect format - too many semicolons", self.cp.parse)

    def testParseInlineConfigurationWith3semicolons(self):
        self.cp = configurationParser.ConfigurationParser("oraclehr;hr;hrdb.example.com;script")
        self.assertRaisesRegexp(ValueError, "Configuration on line 1 has incorrect format - too few semicolons", self.cp.parse)

    def testParseInlineConfigurationWith3semicolonsOnSecondLine(self):
        self.cp = configurationParser.ConfigurationParser("oracle;hr;hr;hrdb.example.com;script\noracle;hrhr;hrdb2.example.com;script")
        self.assertRaisesRegexp(ValueError, "Configuration on line 2 has incorrect format - too few semicolons", self.cp.parse)

    def testFileConfigurationWhenFileDoesNotExists(self):
        self.cp = configurationParser.ConfigurationParser("@/tmp/nonexistent.sql")
        self.assertRaisesRegexp(ValueError, "Configuration file /tmp/nonexistent.sql does not exists!", self.cp.parse)

    def testConfigurationParserWithSimpleConfigurationBeforeParsing(self):
        self.cp = configurationParser.ConfigurationParser("oracle;hr;hrpwd;hrdb.example.com;script")
        self.assertListEqual(self.cp.databases, [])

    def testConfigurationParserWithCorrectSingleLineConfiguration(self):
        self.cp = configurationParser.ConfigurationParser("oracle;hr;hrpwd;hrdb.example.com;script")
        self.cp.parse()
        self.d = database.Database("oracle","hr","hrpwd","hrdb.example.com","script")
        self.assertListEqual(self.cp.databases, [self.d])

    def testConfigurationParserWithCorrectMultipleLineConfiguration(self):
        self.cp = configurationParser.ConfigurationParser("oracle;hr;hrpwd;hrdb.example.com;script\noracle;hr2;hrpwd2;hrdb2.example.com;script2")
        self.cp.parse()
        self.d1 = database.Database("oracle","hr","hrpwd","hrdb.example.com","script")
        self.d2 = database.Database("oracle","hr2","hrpwd2","hrdb2.example.com","script2")
        self.assertListEqual(self.cp.databases, [self.d1, self.d2])
        

    def testFileConfigurationParserWithCorrectSingleLineConfiguration(self):
        filename = '/tmp/test1.txt'
        self.f = open(filename, 'w')
        self.f.write("oracle;hr;hrpwd;hrdb.example.com;script\n")
        self.f.close()

        self.cp = configurationParser.ConfigurationParser('@' + filename)
        self.cp.parse()
        self.d = database.Database("oracle","hr","hrpwd","hrdb.example.com","script")
        self.assertListEqual(self.cp.databases, [self.d])
        os.remove(filename)

    def testFileConfigurationParserWithCorrectMultipleLineConfiguration(self):
        filename = '/tmp/test2.txt'
        self.f = open(filename, 'w')
        self.f.write("oracle;hr;hrpwd;hrdb.example.com;script\noracle;hr2;hrpwd2;hrdb2.example.com;script2")
        self.f.close()

        self.cp = configurationParser.ConfigurationParser('@' + filename)
        self.cp.parse()
        self.d1 = database.Database("oracle","hr","hrpwd","hrdb.example.com","script")
        self.d2 = database.Database("oracle","hr2","hrpwd2","hrdb2.example.com","script2")
        self.assertListEqual(self.cp.databases, [self.d1, self.d2])
        os.remove(filename)



suite = unittest.TestLoader().loadTestsFromTestCase(TestConfigurationParser)
unittest.TextTestRunner(verbosity=2).run(suite)

