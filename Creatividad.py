from random import *
x=raw_input('Ingrese nombre de la historia:')
def crear_personaje(m):
    name=raw_input('ingrese nombre del personaje:')
    gen=raw_input('ingrese genero del personaje:')
    raz=raw_input('ingrese raza del personaje:')
    sheet=open('char_'+name+'_'+x+'.txt','a')
    sheet.write('nombre:'+name+'\n')
    sheet.write('genero:'+gen+'\n')
    sheet.write('moral:'+str(choice(range(-11,11)))+'\n')
    sheet.write('fuerza:'+str(choice(range(1,11)))+'\n')
    sheet.write('percepcion:'+str(choice(range(1,11)))+'\n')
    sheet.write('resistencia:'+str(choice(range(1,11)))+'\n')
    sheet.write('carisma:'+str(choice(range(1,11)))+'\n')
    sheet.write('inteligencia:'+str(choice(range(1,11)))+'\n')
    sheet.write('agilidad:'+str(choice(range(1,11)))+'\n')
    sheet.close()
    return sheet

def modificar_per(archivo_texto):
    name='ingrese nombe personaje:'
    c_sheet=open
    o_sheet=open('char_'+name+'_'+x+'.txt','r')
