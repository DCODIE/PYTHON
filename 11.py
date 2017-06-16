#GUI in python to  dynamically print an upcounter until stop button in pressed
from tkinter import *
counter = 0
def counter_label(labe):
  counter = 0
  def count():
    global counter
    counter += 1
    labe.config(text=str(counter), width=10,font=("Times New Roman",150),fg="Red")
    labe.after(10, count)#time duration
  count()
root = Tk()
root.title("UP COUNTER")
labe = Label(root)
labe.pack()
counter_label(labe)
button = Button(root, text='STOP',font=("Times New Roman",30), command=root.destroy)
button.pack()
root.mainloop()
