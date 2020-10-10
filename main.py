from tkinter import *
   
root = Tk() 

root.title("School Planer") 
root.geometry('1280x720') 

header = Label(root, text="The best School Planer").pack()

info = Label(root, text="Add or Remove a Lesson").pack()

def callback():
	subject = input('What subject do you want to add?\n')
	
	

b = Button (root, text = 'Add a subject', command = callback).pack(side = BOTTOM)

root.mainloop()
