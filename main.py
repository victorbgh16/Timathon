from tkinter import *
   
root = Tk()

def clock():
    t=time.strftime('%I:%M:%S',time.localtime())
    if t!='':
        label1.config(text=t,font='times 25')
    root.after(100,clock)
label1=Label(root,justify='center')
label1.pack()
clock()

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
