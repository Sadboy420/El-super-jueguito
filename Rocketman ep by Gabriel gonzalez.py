from random import choice
def crear_personaje():
    Personajes=open('personajes.txt','a')
    nombre = raw_input("Ingrese nombre del personaje:")
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
    return Personajes
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
        break
#Hecho por Gabriel Gonzalez
#Contacto: xD
        
