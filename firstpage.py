#import module from tkinter for UI
from tkinter import *
#from playsound import playsound
import os
#from datetime import datetime
#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("300x300")

def function1():
    
    os.system("py dataset_capture.py")
    
def function2():
    
    os.system("py training_dataset.py")

def function3():

    os.system("py recognizer.py")
    #playsound('sound.mp3')

def function5():    
   os.startfile(os.getcwd()+"/developers/diet1frame1first.html");
   
def function6():

    root.destroy()

def attend():
    os.startfile(os.getcwd()+"/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xls')

#setting title for the window
root.title("AI Face Recognition Attendance- OFCd")

#creating a text label
Label(root, text="AI Face Recognition Attendance- OFCd",font=("open sans",20),fg="white",bg="#344ea9",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Create User",font=("open sans",20),bg="#bfe8ec",fg='black',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Submit Users",font=("open sans",20),bg="#bfe8ec",fg='black',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Mark Attendance",font=('open sans',20),bg="#bfe8ec",fg="black",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('open sans',20),bg="#344ea9",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()
