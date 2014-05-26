import unittest
from pysqlall import database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.d = database.Database("oracle", "orauser", "orapwd", "testdb.example.com", "/tmp/script.sql")

    def tearDown(self):
        pass

    def testCreation(self):
        self.assertIsInstance(self.d, database.Database)

    def testStrMethod(self):
        self.assertEquals(str(self.d), "{'username': 'orauser', 'connection': 'testdb.example.com', 'password': 'orapwd', 'type': 'oracle', 'script': '/tmp/script.sql'}")

        

class TestDatabaseEquals(unittest.TestCase):

    def setUp(self):
        self.d = database.Database("oracle", "orauser", "orapwd", "testdb.example.com", "/tmp/script.sql")

    def testEqualsMethod(self):
        self.d2 = database.Database("oracle", "orauser", "orapwd", "testdb.example.com", "/tmp/script.sql")
        self.assertEquals(self.d, self.d2)

    def testNotEqualsWithDifferentUsername(self):
        self.d2 = database.Database("oracle", "oravajko", "orapwd", "testdb.example.com", "/tmp/script.sql")
        self.assertNotEquals(self.d, self.d2)

    def testNotEqualsWithDifferentPassword(self):
        self.d2 = database.Database("oracle", "orauser", "orasecretpwd", "testdb.example.com", "/tmp/script.sql")
        self.assertNotEquals(self.d, self.d2)

    def testNotEqualsWithDifferentType(self):
        self.d2 = database.Database("mysql", "orauser", "orapwd", "testdb.example.com", "/tmp/script.sql")
        self.assertNotEquals(self.d, self.d2)

    def testNotEqualsWithDifferentConnection(self):
        self.d2 = database.Database("oracle", "orauser", "orapwd", "wtfdb.example.com", "/tmp/script.sql")
        self.assertNotEquals(self.d, self.d2)

    def testNotEqualsWithDifferentScript(self):
        self.d2 = database.Database("oracle", "orauser", "orapwd", "testdb.example.com", "/tmp/anotherscript.sql")
        self.assertNotEquals(self.d, self.d2)

#if __name__ == '__main__':
#    unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(TestDatabase)
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDatabaseEquals))
unittest.TextTestRunner(verbosity=2).run(suite)

