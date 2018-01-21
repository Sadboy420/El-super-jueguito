from random import *
from Tkinter import *

v0=Tk()
v0.config(bg='red')
b1=Button(v0,text="dado de 20",command=choice(range(1,21))).pack()
b2=Button(v0,text="dado de 6",command=choice(range(1,7))).pack()
b3=Button(v0,text="dado de 4",command=choice(range(1,5))).pack()
b4=Button(v0,text="dado de 10",command=choice(range(1,11))).pack()
b5=Button(v0,text="dado de 12",command=choice(range(1,12))).pack()
b6=Button(v0,text="dado de 8",command=choice(range(1,9))).pack()
b7=Button(v0,text='cerrar program',command=exit)
v0.mainloop()
