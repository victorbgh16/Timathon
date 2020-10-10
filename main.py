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

header = Label(root, text="The best School Planer")
header.pack()

info = Label(root, text="Add or Remove a Lesson")
info.pack()

def addButtonpressed():
	result=subjectInput.get("1.0","end")
	print(result)

subjectInput = Text(root, height=1)
subjectInput.pack()

addButton = Button (root, text = 'Add', command = addButtonpressed)
addButton.pack()

root.mainloop()
