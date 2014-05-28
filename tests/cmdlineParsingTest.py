import unittest
#from pysqlall import createParser
from pysqlall.pysqlall import createParser

class TestCommandLine(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        parser = createParser()
        cls.parser = parser

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCommandLineParsing(self):
        args = self.parser.parse_args(['-u', 'orauser', '-p', 'orapwd', '-d', 'hrdb.example.com', '-s', '/tmp/script.sql'])
        self.assertEquals(args.username, 'orauser')
        self.assertEquals(args.password, 'orapwd')
        self.assertEquals(args.database, 'hrdb.example.com')
        self.assertEquals(args.script, '/tmp/script.sql')


suite = unittest.TestLoader().loadTestsFromTestCase(TestCommandLine)
unittest.TextTestRunner(verbosity=2).run(suite)

