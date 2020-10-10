from tkinter import *
import time
   
root = Tk()

def clock():
	t=time.strftime('%I:%M:%S',time.localtime())
	if t!='':
		label1.config(text=t,font='times 25')
	root.after(100,clock)
label1=Label(root,justify='center')
label1.pack()
clock()

root.title("School Planer") 
root.geometry('1280x720') 

header = Label(root, text="The best School Planer").pack()

info = Label(root, text="Add or Remove a Lesson").pack()

def addButtonpressed():
	result=textExample.get("1.0","end")
	print(result)

subjectInput = Text(root, height=1, width=10, text="Read", command=addButtonpressed)

addButton = Button (root, text = 'Add', command = addButtonpressed).pack()

root.mainloop()
