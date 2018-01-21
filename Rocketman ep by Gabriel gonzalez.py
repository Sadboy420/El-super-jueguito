from random import choice
from Tkinter import *

def crear_personaje(x):
    Personajes=open(x+'_personajes.txt','a')
    nombre = raw_input("Ingrese nombre del personaje:")
    invent=open('Inventario_'+nombre+'.txt','r')
    invent.close()
    stats=dict()
    gen=dict()
    raza=raw_input('ingrese raza del personaje:')
    vida= choice(range(200))
    fuerza=choice(range(1,11))
    percepcion=choice(range(1,11))
    resistencia=choice(range(1,11))
    carisma=choice(range(1,11))
    inteligencia=choice(range(1,11))
    agilidad=choice(range(1,11))
    suerte=choice(range(1,11))
    stats['vida']=vida
    stats['fuerza']=fuerza
    stats['percepcion']=percepcion
    stats['resistencia']=resistencia
    stats['carisma']=carisma
    stats['inteligencia']=inteligencia
    stats['agilidad']=agilidad
    stats['suerte']=suerte
    stats2=[raza,stats]
    gen[nombre]=stats2
    Personajes.write(str(gen)+'\n')
    Personajes.close()
    return Personajes,nombre

def crear_item():
    var=raw_input('ingrese nombre el personaje:')
    nig=open('Inventario_'+var+'.txt','a')
    item=raw_input('ingrese nombre del item a crear:')
    
    
    return

def ver_inv_pers():
    var=raw_input('ingrese nombre el personaje:')
    nig=open('Inventario_'+var+'.txt','r')
    for linea in nig:
        print linea
    nig.close()
    return

def historia(x):
    while True:
        h=open(x+'_historia.txt','a')
        text=raw_input('Ingrese hechos para salir escriba guardar:')
        if text=='guardar':
            h.close()
            break
        else:
            h.write(text+'\n')
    return h

#v0=Tk()
#v0.config(bg='red')
#v0.geometry('500x500')
#b1=Button(v0,text="ir a los dados",command=dado())
#v1=Toplevel(v0)
#v0.mainloop()
uni=raw_input('ingrese nombre del universo: ')
while True:
    print '|-------------------------------------------------|\n|Crear personaje: 1 \n|Iniciar/Resumir historia:2 \n|Ver inventario de un personaje: 3\n|Dar item a un personaje: 4\n|Ver personajes: 5\n|Deletea tus personajes: 6\n|Acabar con mi vida: 7\n|-------------------------------------------------|'
    xd= int(raw_input(' Ingrese opcion:'))
    if xd== 1:
        crear_personaje(uni)
    if xd==5:
        xdd=open(uni+'_personajes.txt','r')
        for linea in xdd:
            print linea
    if xd==2:
        historia(uni)
    if xd==3:
        ver_inv_pers()
    if xd==4:
        crear_item()
    if xd==6:
        print '¿Estas seguro?'
        nya=str(raw_input())
        if nya=='si':
             deletiao=open(uni+'.txt','w')
             deletiao.close()
        if nya=='no':
            print ':('
    if xd==7:
       break
#Hecho por Gabriel Gonzalez
#Contacto: xD
        
