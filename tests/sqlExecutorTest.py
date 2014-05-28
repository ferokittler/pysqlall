import unittest
from pysqlall import sqlExecutor, database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.d = database.Database("oracle", "orauser", "orapwd", "testdb.example.com", "/tmp/script.sql")

    def tearDown(self):
        pass

    def testCreation(self):
        self.se = sqlExecutor.SqlExecutor(self.d)
        self.assertEquals(self.d, self.se.database)

    def testResultCodeBeforeExecutingSqlCode(self):
        self.se = sqlExecutor.SqlExecutor(self.d)
        self.assertIsNone(self.se.returnCode)

    def testResultMessageBeforeExecutingSqlCode(self):
        self.se = sqlExecutor.SqlExecutor(self.d)
        self.assertIsNone(self.se.returnMessage)


suite = unittest.TestLoader().loadTestsFromTestCase(TestDatabase)
unittest.TextTestRunner(verbosity=2).run(suite)

