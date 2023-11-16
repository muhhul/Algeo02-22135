
from pymongo.database import Database
from config.config import get_db_connection
from fastapi import Depends


class Repository:
    def __init__(self,db : Database = Depends(get_db_connection)):
        self.transaction = db.get_collection("transaction")
        self.dataBaseTekstur = db.get_collection("dataTekstur")
        self.dataBaseColour = db.get_collection("dataColour")