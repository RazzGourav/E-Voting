from sklearn.neighbors import KNeighborsClassifier
from time import sleep

import cv2 as cv
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from win32com.client import Dispatch


def speak(str1):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)


video = cv.VideoCapture(0)
facedetect = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
if not os.path.exists('data/'):
    os.makedirs('data/')

with open('data/names.pkl', 'rb') as f:
    LABELS = pickle.load(f)

with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)
speak("WELCOME TO THE SMART VOTING SYSTEM")
imgBackground = cv.imread("background.png")

COL_NAMES = ['NAME', 'VOTE', 'DATE', 'TIME']

def check_if_exists(value):
    try:
        with open("Votes.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row and row[0] == value:
                    return True
    except FileNotFoundError:
        print("File not found or unable to open the CSV file.")
    return False

while True:
    ret, frame = video.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    
    output = None  # Initialize output to a default value
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]
        resized_img = cv.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
        output = knn.predict(resized_img)
        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")
        exist = os.path.isfile("Votes.csv")
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)
        cv.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
        cv.rectangle(frame, (x, y-40), (x+w, y), (50, 50, 255), -1)
        cv.putText(frame, str(output[0]), (x, y-15), cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
        cv.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)
        attendance = [output[0], timestamp]
        
    imgBackground[370:370 + 480, 225:225 + 640] = frame
    cv.imshow('frame', imgBackground)
    k = cv.waitKey(1)
    
    if output is not None:
        voter_exist = check_if_exists(output[0])
        if voter_exist:
            speak("YOU HAVE ALREADY VOTED")
            speak("Thank You, Have A Nice Day Ahead.")
            break

        if k == ord('1'):
            speak("YOUR VOTE HAS BEEN RECORDED")
            time.sleep(5)
            if exist:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    attendance = [output[0], "BJP", date, timestamp]
                    writer.writerow(attendance)
            else:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(COL_NAMES)
                    attendance = [output[0], "BJP", date, timestamp]
                    writer.writerow(attendance)
            speak("You Have Successfully voted to BJP")
            speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS, Have A Nice Day Ahead")
            break

        if k == ord('2'):
            speak("YOUR VOTE HAS BEEN RECORDED")
            time.sleep(5)
            if exist:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    attendance = [output[0], "CONGRESS", date, timestamp]
                    writer.writerow(attendance)
            else:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(COL_NAMES)
                    attendance = [output[0], "CONGRESS", date, timestamp]
                    writer.writerow(attendance)
            speak("You Have Successfully voted to CONGRESS")
            speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS, Have A Nice Day Ahead")
            break

        if k == ord('3'):
            speak("YOUR VOTE HAS BEEN RECORDED")
            time.sleep(5)
            if exist:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    attendance = [output[0], "AAP", date, timestamp]
                    writer.writerow(attendance)
            else:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(COL_NAMES)
                    attendance = [output[0], "AAP", date, timestamp]
                    writer.writerow(attendance)
            speak("You Have Successfully voted to AAP")
            speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS, Have A Nice Day Ahead")
            break

        if k == ord('4'):
            speak("YOUR VOTE HAS BEEN RECORDED")
            time.sleep(5)
            if exist:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    attendance = [output[0], "NOTA", date, timestamp]
                    writer.writerow(attendance)
            else:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(COL_NAMES)
                    attendance = [output[0], "NOTA", date, timestamp]
                    writer.writerow(attendance)
            speak("You Have Successfully voted to NOTA")
            speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS, Have A Nice Day Ahead")
            break

video.release()
cv.destroyAllWindows()