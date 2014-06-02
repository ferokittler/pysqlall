import unittest
from pysqlall import pysqlall
from pysqlall.pysqlall import createParser

class PysqlallTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreation(self):
        self.parser = createParser()
        self.args = self.parser.parse_args(['-u', 'orauser', '-p', 'orapwd', '-d', 'hrdb.example.com', '-s', '/tmp/script.sql'])
        self.p = pysqlall.Pysqlall(self.args)
        self.assertIsInstance(self.p, pysqlall.Pysqlall)


        


suite = unittest.TestLoader().loadTestsFromTestCase(PysqlallTest)
unittest.TextTestRunner(verbosity=2).run(suite)
