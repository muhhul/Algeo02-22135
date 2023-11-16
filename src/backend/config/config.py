import pymongo

client = pymongo.MongoClient("mongodb+srv://predatorfocus17:muhhul@clusterdata.adbmei2.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("dataSetImg")
# transaction = db.get_collection("transaction")
# dataBaseTekstur = db.get_collection("dataTekstur")

def get_db_connection():
    return db