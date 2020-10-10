from tkinter import *
   
root = Tk() 

root.title("School Planer") 
root.geometry('1280x720') 

header = Label(root, text="The best School Planer")
header.grid()

info = Label(root, text="Add or Remove a Lesson")
info.grid()

root.mainloop()
