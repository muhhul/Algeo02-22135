from dataclasses import Field
from typing import Optional
from bson import ObjectId
from fastapi import FastAPI
from pydantic import BaseModel, BeforeValidator, ConfigDict, parse_obj_as
from enum import Enum
from typing import Annotated
import pymongo
import driver
import os
import cv2
import numpy as np
import CBIR_colour


app = FastAPI()

class Tipe(str,Enum):
    def __str__(self):
        return str(self.value)
    INCOME = "INCOME"
    PURCHASE = "PURCHASE"
    INVEST = "INVEST"

class inputTransaction(BaseModel):
    tipe:Tipe
    amount:int
    method:Optional[str]

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    
    @classmethod
    def validate(cls,v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid Object")
        return ObjectId(v)
    
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

# class Transaction(BaseModel):
#     id: PyObjectId 
#     tipe:Tipe
#     amount:int
#     method:Optional[str]
#     class Config:
#         json_encoders = {ObjectId: str}
class dataTekstur(BaseModel):
    contrast:float
    homogency:float
    entropy:float
    filepath:str


client = pymongo.MongoClient("mongodb+srv://predatorfocus17:muhhul@clusterdata.adbmei2.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("dataSetImg")
transaction = db.get_collection("transaction")
dataBaseColour = db.get_collection("dataColour")
dataBaseTekstur = db.get_collection("dataTekstur")


sim = []
data_directory = "D:\\Hul\\ITB\\Akademik\\S3\\Algeo\\Tubes\\Tubes2\\Algeo02-22135\\backend\\dataset"
list_of_files = os.listdir(data_directory)

dataset = []


# for filename in list_of_files:
#     print(filename)
#     dataset_image = cv2.imread(os.path.join(data_directory, filename))
#     dataset_colour = CBIR_colour.calculate_histogram(dataset_image)
#     data:dataColour

#     dataBaseColour.insert_one(my_dict.dict())

# for filename in list_of_files:
#     print(filename)
#     dataset_image = cv2.imread(os.path.join(data_directory, filename))
#     dataset_tekstur = driver.tekstur(dataset_image)
#     data = dataTekstur(contrast=dataset_tekstur[0],homogency=dataset_tekstur[1],entropy=dataset_tekstur[2],filepath=filename)
#     dataset.append(data)
#     dataBaseTekstur.insert_one(data.dict())
# @app.get('/transaction')
# # async def root():
# #     return {"message":"hello world"}
# # Query param
# def get_transaction(tipe:str,amount:int):
#     return f"balikan transaksi dengan tipe {tipe} dan amount {amount}"

# # Path param
# @app.get('/transaction/{tipe}')
# def get_transaction(tipe:str):
#     return f"balikan transaksi dengan tipe {tipe}"


# @app.post('/transaction')
# def insert_transaction(input_transaction:inputTransaction):
#     transaction.append(input_transaction)
#     return transaction


listt = []
transaction_data = {
    "tipe": "INCOME",
    "amount": 100,
    "method": "credit"
}
trransaction = inputTransaction(tipe="INCOME", amount=100, method="credit")
listt.append(trransaction)
transaction_data = {
    "tipe": "INVEST",
    "amount": 3,
    "method": "credit"
}
# trransaction = inputTransaction(**transaction_data)
trransaction = inputTransaction(tipe="INVEST", amount=120, method="credit")
listt.append(trransaction)
for obj in listt:
    transaction.insert_one(obj.dict())
@app.post('/transaction')
def insert_transaction():
    listt = []
    transaction_data = {
        "tipe": "INCOME",
        "amount": 100,
        "method": "credit"
    }
    trransaction = inputTransaction(tipe="INCOME", amount=100, method="credit")
    listt.append(trransaction)
    transaction_data = {
        "tipe": "INVEST",
        "amount": 3,
        "method": "credit"
    }
    # trransaction = inputTransaction(**transaction_data)
    trransaction = inputTransaction(tipe="INVEST", amount=120, method="credit")
    listt.append(trransaction)
    for obj in listt:
        transaction.insert_one(obj.dict())
    # transaction.insert_one(dict(listt))
    # return input_transaction

# @app.get('/transaction')
# def get_transaction(tipe:Optional[Tipe] = None):
#     if tipe is not None:
#         result_filter = []
#         for t in transaction:
#             t = inputTransaction.parse_obj(t)
#             if t.tipe == tipe:
#                 result_filter.append(t)
#     else:
#         result_filter=transaction
#     return result_filter

@app.get('/tekstur')
def get_tekstur(tipe:Optional[Tipe] = None):
    result_filter = dataBaseTekstur.find({})
    result_filter = list(result_filter)

    vektor1 = [33594549,-910456.3650100988,65645.00094583261]
    # for r in result_filter:
    #     r["_id"] = str(r["_id"])
    arrHasil = []
    file=[]
    sim = []
    for i in range(len(result_filter)):
        vektor2 = [result_filter[i].get('contrast'),result_filter[i].get('homogency'),result_filter[i].get('entropy')]
        hasil = driver.compare(vektor1,vektor2)*100
        sim.append(hasil)
        file.append(result_filter[i].get('filepath'))
    sorted_indices = np.argsort(sim)[::-1]
    sorted_similarities = np.sort(sim)[::-1]
    sorted_filenames = [file[i] for i in sorted_indices]
    for i in range(len(result_filter)):
        sim=[]
        sim.append(sorted_similarities[i])
        sim.append(sorted_filenames[i])
        arrHasil.append(sim)
    
    return arrHasil
    
@app.post('/tekstur')
def insert_tekstur(data_directory):
    list_of_files = os.listdir(data_directory)
    i=0
    for filename in list_of_files:
        i=i+1
        if(i==5):
            break
        print(filename)
        dataset_image = cv2.imread(os.path.join(data_directory, filename))
        dataset_image = cv2.resize(dataset_image,(0,0),fx=0.5,fy=0.5)
        dataset_tekstur = driver.tekstur(dataset_image)
        data = dataTekstur(contrast=dataset_tekstur[0],homogency=dataset_tekstur[1],entropy=dataset_tekstur[2],filepath=filename)
        dataBaseColour.insert_one(data.dict())