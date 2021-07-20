from os import name
import cv2
import dropbox
import time
import random

start_time = time.time()
def take_snapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        image_name = "img"+ str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time = time.time
        result = False
    return image_name
    print("SnapShot Taken :(")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(image_name):
     acess_token = "sl.A0j6uOCPoaVQ2PISfW3ybfw4wzt_E0ajc8chPF59G1ffRFkX8FAvw27Z5OcSlSkb9m0NPmGlQIUOlatpa_VOFfwOWXr9hw9hsu-SjL2lhVIMuAN41-1zicsJhB01SJhsbIt26h8"
     file = image_name
     file_from = file
     file_to = "/newFolder1/"+(image_name)
     dbx = dropbox.Dropbox(acess_token)
     
     with open(file_from, "rb")as f:
         dbx.files_upload(f.read().file_to, mode= dropbox.files.WriteMode.overWrite)
         print ("File Uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=1):
            name= take_snapshot()
            upload_file(name)

main() 