# Import OpenCV2 for image processing
import cv2
import os, sys
from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="python",
  passwd="python",
  database="python-face"
)

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

def submit():    
  face_id = textentry.get()
  name = nameentry.get()
  section = sectionentry.get()
  if not face_id:
   window.destroy()
  else:
   mycursor = mydb.cursor()
   sql = "SELECT * FROM reg_users WHERE personal_no = %s"
   val = (face_id,)
   mycursor.execute(sql, val)
   ct= mycursor.fetchall()
   row = mycursor.rowcount
   print(row, "rows found")
   if row <= 0:
#face_id=input('enter your personal no')
# Start capturing video 
         vid_cam = cv2.VideoCapture(0)
# Detect object in video stream using Haarcascade Frontal Face
         face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Initialize sample face image
         count = 0
         assure_path_exists("dataset/")
         
# Start looping
         while(True):
             _, image_frame = vid_cam.read()
             gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
             faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
             for (x,y,w,h) in faces:# Loops for each faces
                 cv2.rectangle(image_frame, (x,y), (x+w,y+h), (0,0,255), 2)# Crop the image frame into rectangle
                 count += 1
                 cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])# Save the captured image into the datasets folder
                 font = cv2.FONT_HERSHEY_SIMPLEX # Display the video frame, with bounded rectangle on the person's face
                 cv2.putText(image_frame,str(face_id),(x,y-10),font,1,(0,0,255),2)
                 cv2.imshow('frame', image_frame)
             
             if cv2.waitKey(100) & 0xFF == ord('q'):# To stop taking video, press 'q' for at least 100ms
                 break
             elif count>=40: # If image taken reach 100, stop taking video
                 break 
                 #print("Successfully Captured")

         mycursor = mydb.cursor()
         sql = "INSERT INTO reg_users (personal_no, name, section) VALUES (%s, %s, %s)"
         val = (face_id, name, section)
         mycursor.execute(sql, val)
         mydb.commit()
         vid_cam.release() # Stop video
         cv2.destroyAllWindows() # Close all started windows
         window.destroy()
   else:
         def ok():
             msg.destroy()
             window.destroy()
         msg=Tk()
         msg.configure(background="white")
         msg.title("Error")
         Label(msg, text="User Already Registered",font=("arial",20),fg="black",bg="white",height=1).grid(row=1,sticky=N+E+W+S,padx=10,pady=10)
         Button(msg,text="OK",font=('arial',15),bg="#344ea9",fg="white",command=ok).grid(row=2,sticky=N+E+W+S,padx=10,pady=10)
         msg.mainloop()
         print("User Registered")


def exit():
    window.destroy()

window=Tk()
window.title("Create User")
window.configure(background="white")
Label(window, text="Enter Personal No.",font=("open sans",10),fg="black",bg="white",height=1).grid(row=3,column=1,sticky=N+E+W+S,padx=5,pady=5)
textentry = Entry(window,width=15,font=('open sans',20),bg="white",fg="blue")
textentry.grid(row=3,column=2,sticky=W,padx=5,pady=3)
Label(window, text="Enter Name",font=("open sans",10),fg="black",bg="white",height=1).grid(row=4,column=1,sticky=N+E+W+S,padx=5,pady=5)
nameentry = Entry(window,width=20,font=('open sans',20),bg="white",fg="blue")
nameentry.grid(row=4,column=2,sticky=W,padx=5,pady=3)
Label(window, text="Enter Section",font=("open sans",10),fg="black",bg="white",height=1).grid(row=5,column=1,sticky=N+E+W+S,padx=5,pady=5)
sectionentry = Entry(window,width=20,font=('open sans',20),bg="white",fg="blue")
sectionentry.grid(row=5,column=2,sticky=W,padx=5,pady=3)
Button(window,text="Submit",font=('open sans',15),bg="#344ea9",fg="white",command=submit).grid(row=7,column=2,sticky=E+W+S,padx=3,pady=3)
#Button(window,text="Exit",font=('open sans',15),bg="maroon",fg="white",command=exit).grid(row=6,sticky=E+W+S,padx=3,pady=3)
window.mainloop()
