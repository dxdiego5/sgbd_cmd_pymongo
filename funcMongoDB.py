import pymongo
from conectionDB import ConnectionMongoDB

connection_db = ConnectionMongoDB().get_connection()

# list all databases mongo registreds array data
def list_databases():
    return connection_db.list_database_names()

# list all collections of database specific
def list_collections_db(dbname):
    return connection_db[dbname].list_collection_names()

# delete collections of database specific
def delete_collection(dbname, collection):
    data = connection_db[dbname]
    data[collection].drop()
    return

def delete_database(dbname):
    return connection_db.drop_database(dbname)

def create_collection_and_database(dbname, collection='test'):
    data = connection_db[dbname]
    data[collection].insert_one(
        {
            "_collection_name": collection,
        }
    )
    return

def create_document(dbname, collection, info):
    data = connection_db[dbname]
    data[collection].insert_one(
        info
    )
    return


def list_all_document(dbname, collection, limit=0):
    data = connection_db[dbname]
    return data[collection].find({}).limit(limit)


def filtered_document(dbname, collection, key, value, limit=0):
    data = connection_db[dbname]
    info = data[collection].find(
            {
                key:{"$eq": value}
            }
        ).limit(limit)
    return info

def delete_document(dbname, collection, key, value):
    data = connection_db[dbname]
    try:
        data[collection].delete_many({key: {"$eq": value}})
        return 'DOCUMENTOS DELETADOS COM SUCESSO'
    except:
        return 'Dados para DELEÇÃO podem estar incorretos'

