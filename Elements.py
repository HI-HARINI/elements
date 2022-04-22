from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.geometry("600x600")
root.title("Dynamic Elements")

elements=["Label","Button","Dropdown"]
selectedval=StringVar()

dropdown=ttk.Combobox(root, values=elements, textvariable=selectedval)
dropdown.pack()

class CreateElements():
    def __init__(self):
        print("Create Dynamic Elements")
    
    def NewElements(self):
        global dropdown
        element=dropdown.get()
        if (element=="Label"):
            label=Label(root,text="This is a label")
            label.pack()
        if (element=="Button"):
            button1=Button(root,text="CLICK ME!!",command=self.message)
            button1.pack()
        if (element=="Dropdown"):
            dropdown=ttk.Combobox(root)
            dropdown.pack()
    
    def message(self):
        messagebox.showinfo("New Button","This button is a Dynamic Element")

object1=CreateElements()
button2=Button(root,text="SUPRISE (If you click me)!!",command=object1.NewElements)
button2.pack()
root.mainloop()