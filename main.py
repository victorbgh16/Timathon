from tkinter import *
import time
   
root = Tk()

def clock():
	t = time.strftime('%I:%M:%S',time.localtime())
	if t != '':
		label1.config(text = t,font = 'times 25')
	root.after(100,clock)
label1 = Label(root,justify = 'center')
label1.pack()
clock()

root.title("School Planer") 
root.geometry('1280x720') 

header = Label(root, text = "The best School Planner")
header.pack()

info = Label(root, text = "Add or Remove a Lesson")
info.pack()

def addButtonpressed():
	result = subjectInput.get("1.0","end")
	print(result)
	result_label = Label(root, text = result)
	result_label.pack()

subjectInput = Text(root, height = 1)
subjectInput.pack()

addButton = Button(root, text = 'Add', command = addButtonpressed)
addButton.pack()

def RemoveButtonPressed():
	result2 = RemoveInput.get('1.0', 'end')
	print(result2)

RemoveInput = Text(root, height = 1)
RemoveInput.pack()

RemoveButton = Button(root, text = 'Remove', command = RemoveButtonPressed)
RemoveButton.pack()

def MathsButtonPressed():
	print('maths')
	maths_label = Label(root, text = 'maths')
	maths_label.pack()

MathsButton = Button(root, text = 'add maths', command = MathsButtonPressed)
MathsButton.pack()

def EnglishButtonPressed():
	print('english')
	english_label = Label(root, text = 'english')
	english_label.pack()


EnglishButton = Button(root, text = 'add english', command = EnglishButtonPressed)
EnglishButton.pack()

root.mainloop()

