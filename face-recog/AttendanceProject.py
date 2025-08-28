import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# obtaining the images from the directory
path = '/home/asoliman/project/face_recog/images'
images = []
classNames = []
myList = os.listdir(path)
print(myList)

# Cleaning out the names of the images
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

# Function to find encodings
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

script_dir = os.path.dirname(os.path.abspath(__file__))
attendance_path = os.path.join(script_dir, "Attendance.csv")

def markAttendance(name):
    with open(attendance_path, 'a+', encoding='utf-8') as f:
        myDataList = f.readlines()
        nameList = []
        print(myDataList)
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[1])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'{name},{dtString}')

markAttendance('Elon')

encodeListKnown = findEncodings(images)
print('Encoding complete')

# initiate webcam 
cap = cv2.VideoCapture(0)
while True:

    success, img = cap.read()
    img_s = cv2.resize(img, (0,0), None, 0.25,0.25)
    imgS = cv2.cvtColor(img_s, cv2.COLOR_BGR2RGB)
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1,x2,y2,x1 = faceLoc
            y1,x2,y2,x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)



    cv2.imshow('webcam', img)
    cv2.waitKey(1)

