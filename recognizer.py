import cv2, numpy as np
import xlwrite,firebase.firebase_ini as fire
import time
import sys
from datetime import datetime, date
from playsound import playsound
import mysql.connector

today = date.today()
#dt = today.strftime("%d-%m-%Y")

currTime = datetime.now()
tm = currTime.time()

mydb = mysql.connector.connect(
  host="localhost",
  user="python",
  passwd="python",
  database="python-face"
)

def db_timein(id):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM attandance_data WHERE personal_no = %s && att_date = %s"
    val = (id, today)
    mycursor.execute(sql, val)
    ct= mycursor.fetchall()
    row = mycursor.rowcount
    print(row, "rows found")
    if row <= 0:
        sql = "INSERT INTO attandance_data (personal_no, att_date, time_in) VALUES (%s, %s, %s)"
        val = (id, today, tm)
        mycursor.execute(sql, val)
        mydb.commit()

def db_timeout(id):
    currTime = datetime.now()
    tm = currTime.time()
    mycursor = mydb.cursor()
    sql = "UPDATE attandance_data SET time_out = %s WHERE personal_no = %s && att_date = %s"
    val = (tm, id, today)
    mycursor.execute(sql, val)
    mydb.commit()
    print("i am at timeout")


start=time.time()
period=8
face_cas = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0);
window_name = "AI face Detection"
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
recognizer = cv2.face.LBPHFaceRecognizer_create();
recognizer.read('trainer/trainer.yml');
flag = 0
id=0
filename='filename'
dict = { "item1" :1}
#font = cv2.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 5, 1, 0, 1, 1)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = face_cas.detectMultiScale(gray, 1.3, 7);
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,200,0),2);
        id,conf=recognizer.predict(roi_gray)
        if(conf < 50):
            if((str(id)) not in dict):
                dict[str(id)]=str(id)
                db_timein(id)
                playsound('thank_you.mp3')
                
            else :
                time.sleep(3);
                playsound('youarepresent.mp3')
                db_timeout(id)

        else:
             id = 'Unknown, can not recognize'
             flag=flag+1
             continue
        
        cv2.putText(img,str(id),(x,y-10),font,1,(0,0,200),2)
        #cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,0,255));
    cv2.imshow(window_name,img);
    #cv2.imshow('gray',gray);
    if flag == 10:
        playsound('try_again.mp3')
        print("Try Again")
    #    break;
    #if time.time()>start+period:
    #    break;
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break;
print(dict)
cap.release();
cv2.destroyAllWindows();
