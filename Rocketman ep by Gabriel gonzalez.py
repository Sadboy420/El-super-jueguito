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
    Personajes.close()
    return t
while True:
    print '|-------------------------------------------------|\n|Crear personaje: 1 \n|Ver personajes: 2\n|Deletea tus personajes: 3\n|Acabar con mi vida: 4\n|-------------------------------------------------|'
    xd= int(raw_input(' Ingrese opcion:'))
    if xd== 1:
        crear_personaje()
    if xd==2:
        xdd=open('personajes.txt','r')
        for linea in xdd:
            print linea
    if xd==3:
        print '¿Estas seguro?'
        nya=str(raw_input())
        if nya=='si':
            deletiao=open('personajes.txt','w')
            deletiao.close()
        if nya=='no':
            print ':('
    if xd==4:
        Personajes.close()
        break

        
