from fastapi import FastAPI,UploadFile
app = FastAPI()
from pydantic import BaseModel
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar




class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: str | None = None

# @app.post("/BarCodeImage")
# async def BarCodeImage(item:Item):
#     img = cv2.imdecode(np.frombuffer(await file.read(), np.uint8), -1)

#     decodedObjects = pyzbar.decode(image)
#     for obj in decodedObjects:
#         # print("Type: QRCODE")
#         # print("Data:  b'www.copyassignment.com'")
#         print("Type:", obj.type)
#         print("Data: ", obj.data, "\n")


#     cv2.imshow("Frame", image)
#     cv2.waitKey(0)

@app.post("/barCodeImage/")
async def create_upload_file(file: UploadFile):
    image = cv2.imdecode(np.frombuffer(await file.read(), np.uint8), -1)
    decodedObjects = pyzbar.decode(image)
    data =[]
    for obj in decodedObjects:
        data.append({"type":obj.type,"Data":obj.data})
    
    # cv2.imshow("Frame", image)
    # cv2.waitKey(0)
    return data
        
