from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.configure(bg="#348933")
root.title("Creating new elements!")
class CreateElement():

    def __init__(self):
        self.number = 0
        print("Request to create Element")

    def NewElement(self):
        self.number = self.number + 1
        label = Label(root, text="New Element Created Successfully with the id : "+str(self.number), foreground="red")
        label.pack()
        
        btn = Button(root, text="Click Me", command=self.showMessage)
        btn.pack(padx=10, pady=10)
        
    def showMessage(self):
        messagebox.showinfo(title="Button click", message="Toast showed successfully!")
        
intance_of_CreateElement = CreateElement()

button = Button(root, text="Click me to create new element", background="#193991", borderwidth=1, command=intance_of_CreateElement.NewElement)
button.pack(pady=10)

root.mainloop()