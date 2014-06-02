import argparse
import configuration

# TODO: object design

# Config file example
# database_type;username;password;connection_string:script
# oracle;hr;hr;hrdb.example.com;script;

class Pysqlall(object):
    def __init__(self, args):
        self.configuration = configuration.Configuration(args.database, args.username, args.password, args.script)
        #self.configuration.read()


def createParser():
    parser = argparse.ArgumentParser(description = "Tool for running SQL code on multiple databases")
    parser.add_argument("-u", "--username", help="username for connecting to database")
    parser.add_argument("-p", "--password", help="password for connecting to database")
    parser.add_argument("-d", "--database", help="connection string for database")
    parser.add_argument("-s", "--script", help="file containing SQL code")

    return parser

def main():
    parser = createParser()
    args = parser.parse_args()

    pysqlall = Pysqlall(args)
    

    # Do whatever you need to do
    print "Here comes the sun..."


if __name__ == '__main__':
    main()
#main()
