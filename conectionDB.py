import pymongo
from pymongo.errors import ConnectionFailure

# class private connection database
class ConnectionMongoDB():
    def __init__(self):
        try:
            # verify connection mongodb is available
            self.__conn = pymongo.MongoClient("mongodb://localhost:27017/")
            self.__conn.admin.command('ping')
        except ConnectionFailure:
            print('Não foi encontrada uma conexão com o banco de dados..')
            print(ConnectionFailure)

    def get_connection(self):
        return self.__conn
