import os
import cv2 as cv
from fastapi import FastAPI, UploadFile, File
import uvicorn
from fastapi.encoders import jsonable_encoder

app=FastAPI()
@app.post("/create_file/")
async def image(image:UploadFile=File(...)):
    print(image.file)

    try:
        os.mkdir("image_volume")
        print(os.getcwd())
    except Exception as e:
        print(e)
    file_name=os.getcwd()+"/image_volume/"+image.filename.replace(" ","-")

    with open(file_name,'wb+') as f:
        f.write(image.file.read())
        f.close()
    
    img = cv.imread(file_name)
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    file_name1=os.getcwd()+"/image_volume/"+"grayscale"+image.filename.replace(" ","-")
    cv.imwrite(file_name1,gray)
    
    #cv.imshow('Image',img)
    #cv.imshow('Gray',gray)
    file=jsonable_encoder({"imagePath":file_name1})
    #new_image=await add_image(file)
    return file

if __name__=="__main__":
    host_name=os.environ.get('ENV_HOSTNAME')
    uvicorn.run(app,host=host_name,port=8099)
