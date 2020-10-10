from tkinter import *
   
root = Tk()

time_string = time.strftime('%H:%M:%S')
myvar = Tkinter.Label(root,image = tkimage, text = time_string, compound = Tkinter.CENTER)

root.title("School Planer") 
root.geometry('1280x720') 

header = Label(root, text="The best School Planer").pack()

info = Label(root, text="Add or Remove a Lesson").pack()

subjectInput = Text(root, height=1, width=10, text="Read", command=addButtonpressed)

def addButtonpressed():
	result=textExample.get("1.0","end")
    	print(result)

addButton = Button (root, text = 'Add', command = addButtonpressed).pack()

root.mainloop()
