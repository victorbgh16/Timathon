from tkinter import *
   
root = Tk() 

root.title("School Planer") 
root.geometry('1280x720') 

header = Label(root, text="The best School Planer").pack()

info = Label(root, text="Add or Remove a Lesson").pack()

subjectInput = Text(root, height=1, width=30).pack()

def addButtonpressed():
	print('Test')

addButton = Button (root, text = 'Add', command = addButtonpressed).pack()

def retrieve_input():
	input = self.subjectInput.get('1.0', END)

root.mainloop()
