import random
import unittest
from pysqlall import configuration

class TestConfigurationParsing(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConfigFileDoesNotExists(self):
        self.configuration = configuration.configuration()
        self.assertRaises(IOError, self.configuration.parseConfiguration, '/tmp/nonexistent')
        


#if __name__ == '__main__':
#    unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(TestConfigurationParsing)
unittest.TextTestRunner(verbosity=2).run(suite)

