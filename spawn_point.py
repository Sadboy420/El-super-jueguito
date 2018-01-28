from random import *

def spawn_point():
    x=choice(range(1,101))
    lineas=open('Mapa.txt','r')
    if x<=10:
        for linea in lineas:
            if linea[0:5]=='tier3':
                spawn=linea.strip().split(',')
                z=choice(range(1,len(spawn)+1))
                point=spawn[z]
                lineas.close()
                return point
    if x>10 and x<=25:
        for linea in lineas:
            if linea[0:5]=='tier2':
                spawn=linea.strip().split(',')
                z=choice(range(1,len(spawn)+1))
                point=spawn[z]
                lineas.close()
                return point
    if x>25:
        for linea in lineas:
            if linea[0:5]=='tier1':
                spawn=linea.strip().split(',')
                z=choice(range(1,len(spawn)+1))
                point=spawn[z]
                lineas.close()
                return point

spawn_point()
