import cv2 as cv                        
import pickle                        
import numpy as np
import os

if not os.path.exists('data/'):
    os.makedirs('data/')

video = cv.VideoCapture(0)
facedetect= cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces_data = []

attempts = 0
while attempts < 3:
    name = input("Enter your aadhar number: ")
    
    if name.isdigit() and len(name) == 12:
        print("Valid Aadhar number entered!")
        break
    else:
        attempts += 1
        print("Invalid Aadhar number. Please enter a 12-digit numeric value.")

if attempts == 3:
    print("Too Many Attempts.")
    exit()

framesTotal=51
captureAfterFrame=2

i=0
while True:
    ret, frame = video.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces=facedetect.detectMultiScale(gray, 1.3 ,5)
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]
        resized_img = cv.resize(crop_img, (50, 50))
        if len(faces_data)<= framesTotal and i%captureAfterFrame==0:
            faces_data.append(resized_img)
        i=i+1
        cv.putText(frame, str(len(faces_data)),(50,50),cv.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 1 )
        cv.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 1)


    cv.imshow('frame', frame)
    k=cv.waitKey(1)
    if k== ord('q') or len(faces_data) >= framesTotal:
        break


video.release()
cv.destroyAllWindows()

faces_data = np.asarray(faces_data)
faces_data = faces_data.reshape((framesTotal, -1))
print(faces_data)



if 'names.pkl' not in os.listdir('data/'):
    names=[name]*framesTotal
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)
else:
    with open('data/names.pkl', 'rb') as f:
        names=pickle.load(f)
    names=names+[name]*framesTotal
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)
     

if 'faces_data.pkl' not in os.listdir('data/'):
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces_data, f)
else:
    with open('data/faces_data.pkl', 'rb') as f:
        faces=pickle.load(f)
    faces=np.append(faces, faces_data, axis=0)
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces, f)

if name in names:
    print("Congratulations, You are enrolled Successfully")
    exit()
