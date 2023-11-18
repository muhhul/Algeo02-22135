from dataclasses import Field
from typing import Optional
from bson import ObjectId
from fastapi import FastAPI, File, UploadFile
from matplotlib import image
from pydantic import BaseModel, BeforeValidator, ConfigDict, parse_obj_as
from enum import Enum
from typing import Annotated
import pymongo
import driver
import os
import cv2
import numpy as np
import CBIR_colour
import csv
from PIL import Image
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List
import shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ganti dengan daftar asal yang diizinkan
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
# data_directory = "D:\\Hul\\ITB\\Akademik\\S3\\Algeo\\Tubes\\Tubes2\\Algeo02-22135\\backend\\dataset"
# list_of_files = os.listdir(data_directory)

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
# trransaction = inputTransaction(tipe="INVEST", amount=120, method="credit")
# listt.append(trransaction)
# for obj in listt:
#     transaction.insert_one(obj.dict())

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

# dataAwal = "D:/Hul/ITB/Akademik/S3/Algeo/Tubes/Tubes2/algeo02-22135/src/backend/dataset"
# dataColour = []
# list_of_files = os.listdir(dataAwal)
# for filename in list_of_files:
#     dataset_image = cv2.imread(os.path.join(dataAwal, filename))
#     histogram = CBIR_colour.calculate_histogram(dataset_image)
#     simm=[]
#     simm.append(histogram)
#     simm.append(filename)
#     dataColour.append(simm)

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
def insert_tekstur(data_directory,namaColl):
    # absolute_path = os.path.abspath(data_directory)
    # with open(absolute_path, "r") as file:
    #     list_of_files = file.read()
    list_of_files = os.listdir(data_directory)
    print(data_directory)
    i=0
    dataBaseBaru=db.get_collection(namaColl)
    dataBaseBaru.delete_many({})
    print(len(list_of_files))
    for filename in list_of_files:
        i=i+1
        if(i==10):
            break
        print(filename)
        dataset_image = cv2.imread(os.path.join(data_directory, filename))
        dataset_image = cv2.resize(dataset_image,(0,0),fx=0.5,fy=0.5)
        dataset_tekstur = driver.tekstur(dataset_image)
        data = dataTekstur(contrast=dataset_tekstur[0],homogency=dataset_tekstur[1],entropy=dataset_tekstur[2],filepath=filename)
        dataBaseBaru.insert_one(data.dict())
    return ("sukses uploading gambar")

@app.get('/colour')
def get_colour(data_directory):
    list_of_files = os.listdir(data_directory)
    filename = list_of_files[0]
    input_image = cv2.imread(os.path.join(data_directory, filename))
    sorted_indices, sorted_similarities,sorted_filenames = CBIR_colour.compareimage(input_image, data_directory)
    arrHasil=[]
    for i in range(len(sorted_similarities)):
        sim=[]
        sim.append(sorted_similarities[i])
        sim.append(sorted_filenames[i])
        arrHasil.append(sim)
    return arrHasil

@app.post('/colour')
def insert_colour(data_directory):
    # absolute_path = os.path.abspath(data_directory)
    # with open(absolute_path, "r") as file:
    #     list_of_files = file.read()
    list_of_files = os.listdir(data_directory)
    array=[]
    pathCSV = "D:/Hul/ITB/Akademik/S3/Algeo/Tubes/Tubes2/algeo02-22135/src/backend/dataCSV/data.csv"
    for filename in list_of_files:
        dataset_image = cv2.imread(os.path.join(data_directory, filename))
        histogram = CBIR_colour.calculate_histogram(dataset_image)
        array.append({
            "histogram":histogram,
            "filepath":filename
        })
    with open(pathCSV, 'w', newline='') as csv_file:
        fieldnames = ['histogram', 'filepath']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in array:
            writer.writerow(row)
    return ("sukses uploading gambar")

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    image_content = await file.read()
    nparr = np.frombuffer(image_content, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    vektor1 = driver.tekstur(img)

    result_filter = dataBaseTekstur.find({})
    result_filter = list(result_filter)

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
    
    print(arrHasil)
    
@app.post("/uploadfile2/")
async def create_upload_file(file: UploadFile = File(...)):
    image_content = await file.read()
    arrHasil = []
    nparr = np.frombuffer(image_content, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    sorted_indices, sorted_similarities,sorted_filenames = CBIR_colour.compare_histo_csv(img, pathCSV)
    for i in range(len(sorted_indices)):
        sim=[]
        sim.append(sorted_similarities[i])
        sim.append(sorted_filenames[i])
        arrHasil.append(sim)
    print(arrHasil)

UPLOAD_FOLDER = "upload_images"
@app.post("/upload")
async def upload_folder(folder: UploadFile = File(...)):
    pathold = os.path.join("uploaded_folders")
    shutil.rmtree(pathold)
    folder_path = os.path.join("uploaded_folders", folder.filename.replace('/', '_'))
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
        except OSError as e:
            return {"error": str(e)}
    files = folder.file.read().split(b'\\0')
    for i, file_data in enumerate(files):
        file_path = os.path.join(folder_path, f"{i}.jpg")
        with open(file_path, "wb") as f:
            f.write(file_data)
    insert_tekstur(folder_path,"tesss")
        