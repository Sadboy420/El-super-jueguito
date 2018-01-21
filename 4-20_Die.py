from random import *
from Tkinter import *

def dado4():
    dado4=choice(range(1,5))
    print "Dice(4) rolled a:"
    print dado4
def dado6():
    dado6=choice(range(1,7))
    print "Dice(6) rolled a:"
    print dado6
def dado8():
    dado8=choice(range(1,9))
    print "Dice(8) rolled a:"
    print dado8
def dado10():
    dado10=choice(range(1,11))
    print "Dice (10) rolled a:"
    print dado10
def dado12():
    dado12=choice(range(1,13))
    print "Dice(12) rolled a:"
    print dado12
def dado20():
    dado20=choice(range(1,21))
    print "Dice(20) rolled a:"
    print dado20

w = Tk()

aa = Label(w, text="Select a Dice:",)
aa.pack()

a = Button(w, text =" \n      4       \n",command=dado4,bd=5)
a.pack()
b = Button(w, text =" \n      6       \n",command=dado6,bd=6)
b.pack()
c = Button(w, text =" \n      8       \n ",command=dado8,bd=7)
c.pack()
d = Button(w, text =" \n      10      \n ",command=dado10,bd=8)
d.pack()
e = Button(w, text =" \n      12      \n ",command=dado12,bd=9)
e.pack()
g = Button(w, text =" \n      20      \n ",command=dado20,bd=10)

g.pack()


nm = Label(w, text ="You rolled a: ")
nm.pack()




"""

bb = Button(w, text ="Dado de 6",command=dado6)
bb.pack()
cc = Button(w, text ="Dado de 8",command=dado8)
cc.pack()
dd = Button(w, text ="Dado de 10",command=dado10)
dd.pack()
ee = Button(w, text ="Dado de 12",command=dado12)
ee.pack()
gg = Button(w, text ="Dado de 20",command=dado20)
gg.pack()

"""
w.mainloop()
