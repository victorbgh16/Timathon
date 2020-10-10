from tkinter import *
   
root = Tk()

time_string = time.strftime('%H:%M:%S')
myvar = Tkinter.Label(root,image = tkimage, text = time_string, compound = Tkinter.CENTER)

root.title("School Planer") 
root.geometry('1280x720') 

header = Label(root, text="The best School Planer").pack()

info = Label(root, text="Add or Remove a Lesson").pack()

subjectInput = Text(root, height=1, width=30).pack()

def addButtonpressed():
	print('Test')

addButton = Button (root, text = 'Add', command = addButtonpressed).pack()

def retrieve_input():
	input = self.subjectInput.get('1.0', 'end-1c')

root.mainloop()

# https://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-widget


#from tkinter import *
#root=Tk()
#def retrieve_input():
#    inputValue=textBox.get("1.0","end-1c")
#    print(inputValue)
#
#textBox=Text(root, height=2, width=10)
#textBox.pack()
#buttonCommit=Button(root, height=1, width=10, text="Commit", 
#                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
#buttonCommit.pack()
#
#mainloop()
