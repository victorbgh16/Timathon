from tkinter import *
import time
from tkinter.ttk import Notebook

root = Tk()


def clock():
    t = time.strftime('%I:%M:%S', time.localtime())
    if t != '':
        label1.config(text=t, font='times 25')
    root.after(100, clock)


label1 = Label(root, justify='center')
label1.pack()
clock()

root.title("School Planer")
root.geometry('1280x720')

header = Label(root, text="The best School Planner")
header.pack()

info = Label(root, text="Add or Remove a Lesson")
info.pack()


def addButtonpressed():
    result = subjectInput.get("1.0", "end")
    print(result)
    result_label = Label(root, text=result)
    result_label.pack()


subjectInput = Text(root, height=1)
subjectInput.pack()

addButton = Button(root, text='Add', command=addButtonpressed)
addButton.pack()


def RemoveButtonPressed():
    result2 = RemoveInput.get('1.0', 'end')
    print(result2)


RemoveInput = Text(root, height=1)
RemoveInput.pack()

RemoveButton = Button(root, text='Remove', command=RemoveButtonPressed)
RemoveButton.pack()


def MathsButtonPressed():
    print('maths')
    maths_label = Label(root, text='Maths')
    maths_label.pack()


MathsButton = Button(root, text='add Maths', command=MathsButtonPressed)
MathsButton.pack()


def EnglishButtonPressed():
    print('english')
    english_label = Label(root, text='English')
    english_label.pack()


EnglishButton = Button(root, text='add English', command=EnglishButtonPressed)
EnglishButton.pack()



def BreakButtonPressed():
    print('break')
    break_label = Label(root, text = 'Break')
    break_label.pack()


BreakButton = Button(root, text = 'add a Break', command = BreakButtonPressed)
BreakButton.pack()

frame = Frame(root)
frame.pack(fill = 'both')

tablayout = Notebook(frame)

tab = Frame(tablayout)
tab.pack(fill = 'both')


label = Label(tab, text = 'this is just a test')
label.pack()
tablayout.add(tab, text = 'TAB 1')

tab2 = Frame(tablayout)
tab2.pack(fill = 'both')

label2 = Label(tab2, text='this is the second test')
label2.pack()


tablayout.add(tab2, text='TAB 2')
tablayout.pack(fill='both')

# Python program to create a table 

from tkinter import *


class Table: 
    
    def __init__(self,root): 
        
        # code for creating table 
        for i in range(total_rows): 
            for j in range(total_columns): 
                
                self.e = Entry(root, width=20, fg='blue', 
                            font=('Arial',16,'bold')) 
                
                self.e.grid(row=i, column=j) 
                self.e.insert(END, lst[i][j]) 

# take the data 
lst = [(1,'Raj','Mumbai',19), 
    (2,'Aaryan','Pune',18), 
    (3,'Vaishnavi','Mumbai',20), 
    (4,'Rachna','Mumbai',21), 
    (5,'Shubham','Delhi',21)] 

# find total number of rows and 
# columns in list 
total_rows = len(lst) 
total_columns = len(lst[0]) 

# create root window 
root = Tk() 
t = Table(root) 
root.mainloop() 


root.mainloop()
