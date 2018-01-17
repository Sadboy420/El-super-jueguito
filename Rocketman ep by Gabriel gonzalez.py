#Hecho por Gabriel Gonzalez
#Contacto: xD
from random import choice
Personajes=open('personajes.txt','a')
def crear_personaje():
    n = raw_input("Ingrese nombre del personaje:")
    v = 10
    v+= choice(range(11))
    s = 15
    s+= choice(range(16))
    h = 5
    h+= choice(range(6))
    t = (n,v,s,h)
    print 'Nombre: '+str(t[0])+ '\n'+'Vida: '+str(t[1])+'\n'+'Mana: '+str(t[2])+'\n'+'Estabilidad mental: '+str(t[3])
    Personajes.write('Nombre: '+str(t[0])+ '\n'+'Vida: '+str(t[1])+'\n'+'Mana: '+str(t[2])+'\n'+'Estabilidad mental: '+str(t[3])+'\n'+'--------------------------------------------------'+'\n')
    return t
while True:
    print 'Crear personaje: 1 \n otros: 2'
    xd= int(raw_input('ingrese opcion:'))
    if xd== 1:
        crear_personaje()
    
    else:
        Personajes.close()
        break

        
