import face_recognition
import numpy as np
import cv2

def Train(images):
    encodedList = []
    for x in images:
        img = face_recognition.load_image_file(x)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encd = face_recognition.face_encodings(img)[0]
        encodedList.append(encd)
    return encodedList

def Test(imgLoc, trainedList):
    img = face_recognition.load_image_file(imgLoc)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encoed = face_recognition.face_encodings(img)[0]
    results = face_recognition.compare_faces(trainedList, encoed)
    