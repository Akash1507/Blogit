# Importing the necessary Libraries
import pymongo

# Creating Database class for the project
class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    # Function for establishing connection
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['blogit']

    # Function for Inserting Data
    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    # Function for retrieving all Data
    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    # Function for retrieving single Data
    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
