# PEPE IS CURRENTY IN DEVELOPMENT

from random import *
from Tkinter import *
#SPAWNS STUFF

#LOOT CHANCE STUFF



#BATTLE STUFF
def player_hit_chance():
        luck=choice(range(1,101))
        print "\nPLAYER:"
        if luck<=80:
            crit=choice(range(1,101))
            if crit<=90:
                print "----\nHit!\n----"
            else:
                print "----\nCRITICAL HIT!\n----"
        else:
            print "----\nMiss...\n----"
def foe_common_ai():
    print "\nENEMY:"
    c=choice(range(1,101))
    if c<=70:
        print "----\nAttack! "
        luck=choice(range(1,101))
        if luck>20:
            crit=choice(range(1,101))
            if crit<=10:
                print "CRITICAL HIT!\n----"
            if crit>=11:
                print "Hit!\n----"
        elif luck<=20:
            print "Miss...\n----"

    elif c>70 and c<90:
        print "---\n*Defend*\n----"
    elif c>=90:
        print "---\nSupport: "
        s=choice(range(1,3))
        if s==1:
            print "+ Heal +\n----"
        if s==2:
            print "Foe calls for help!"
            friend=choice(range(1,101))
            if friend<=50:
                print "Another foe joins the battle!\n----"
            elif friend >50:
                print "But nobody came...\n----"
# PSI ENEMY
def foe_pk_ai():

    print "\nPK/PSI ENEMY:"
    c=choice(range(1,101))
    if c<=70:
        print "----\nAttack! "
        luck=choice(range(1,101))
        if luck>20:
            crit=choice(range(1,101))
            if crit<=10:
                print "CRITICAL HIT!\n----"
            if crit>=11 and crit<50 :
                print "Hit!\n----"
            if crit>=50:
                s=choice(range(1,8))
                if s==1:
                    print "PK FIRE!\n----"
                if s==2:
                    print "PK THUNDER!\n----"
                if s==3:
                    print "PSI Shield!\n----"
                if s==4:
                    print "PSI Offence up!\n----"
                if s==5:
                    print "PSI Defence up!\n----"
                if s==6:
                    print "PK STARSTORM!\n----"
                if s==7:
                    print "PSI Healing\n----"
        elif luck<=20:
            print "Miss...\n----"

    elif c>70 and c<90:
        print "---\n*Defend*\n----"
    elif c>=90:
        print "---\nSupport: "
        s=choice(range(1,3))
        if s==1:
            print "+ Heal +\n----"
        if s==2:
            print "Foe calls for help!"
            friend=choice(range(1,101))
            if friend<=50:
                print "Another foe joins the battle!\n----"
            elif friend >50:
                print "But nobody came...\n----"

#DICE STUFF

def coin_toss():
    coin_toss=choice(range(1,3))
    print "--\nCoin landed:"
    if coin_toss==1:
        print "Heads!(YES)"
    if coin_toss==2:
        print "Tails!(NO)"
def dado4():
    dado4=choice(range(1,5))
    print "--\nDice(4) rolled a:"
    print dado4
def dado6():
    dado6=choice(range(1,7))
    print "--\nDice(6) rolled a:"
    print dado6
def dado8():
    dado8=choice(range(1,9))
    print "--\nDice(8) rolled a:"
    print dado8
def dado10():
    dado10=choice(range(1,11))
    print "--\nDice(10) rolled a:"
    print dado10
def dado12():
    dado12=choice(range(1,13))
    print "--\nDice(12) rolled a:"
    print dado12
def dado20():
    dado20=choice(range(1,21))
    print "--\nDice(20) rolled a:"
    print dado20
def dado100():
    dado100=choice(range(1,101))
    print "--\nDice(100) rolled a:"
    print dado100


def loot_chance():
    p = choice(range(1,101))
    #SUPER RARE LOOT
    if p <= 1:
        print "\nSUPER RARE:"
        qv=choice(range(1,101))
        if qv>=75:
            print ' New\n'
        elif qv>25 and qv<75:
            print ' Used\n'
        elif qv<=25:
            print ' Broken\n'
        elif qv==100:
            print ' GOLDEN\n'
    #Rare Weapons & Armor
    elif p <= 5:
        print "----\nRARE:"
        qiv=choice(range(1,101))
        if qiv>=50:
            print ' WEAPON'
            pors=choice(range(1,3))
            if pors==1:
                print "Primary!"
                qivqq=choice(range(1,101))
                qivwbuff=choice(range(1,5))

                if qivqq>=75:
                    print ' New'
                elif qivqq>25 and qiv<75:
                    print ' Used'
                elif qivqq<=25:
                    print ' Broken'
                elif qivqq==100:
                    print ' GOLDEN'


                if qivwbuff==1:
                    print " +ATK\n----"
                elif qivwbuff==2:
                    print " +HP\n----"
                elif qivwbuff==3:
                    print " +DEF\n----"
                elif qivwbuff==4:
                    print " +SP\n----"
            else:
                print "Secondary!"
                qivqq=choice(range(1,101))
                qivwbuff=choice(range(1,5))

                if qivqq>=75:
                    print ' New'
                elif qivqq>25 and qiv<75:
                    print ' Used'
                elif qivqq<=25:
                    print ' Broken'
                elif qivqq==100:
                    print ' GOLDEN'


                if qivwbuff==1:
                    print " +ATK\n----"
                elif qivwbuff==2:
                    print " +HP\n----"
                elif qivwbuff==3:
                    print " +DEF\n----"
                elif qivwbuff==4:
                    print " +SP\n----"
        elif qiv<50:
            print " ARMOR\n"
            qivq=choice(range(1,101))
            qiiiabuff=choice(range(1,5))

            if qiiiabuff==1:
                print " +ATK\n----"
            elif qiiiabuff==2:
                print " +HP\n----"
            elif qiiiabuff==3:
                print " +DEF\n----"
            elif qiiiabuff==4:
                print " +SP\n----"

            if qivq>=75:
                print ' New'
            elif qivq>25 and qiii<75:
                print ' Used'
            elif qivq<=25:
                print ' Broken'
            elif qivq==100:
                print ' GOLDEN'
    #Weapons & Armor
    elif p <= 15:
        qiii=choice(range(1,101))
        if qiii>=50:
            print '----\nWEAPON:'
            porss=choice(range(1,3))
            if porss==1:
                print "Primary!"
                qiii=choice(range(1,101))
                if qiii>=75:
                    print ' New\n----'
                elif qiii>25 and qiii<75:
                    print ' Used\n----'
                elif qiii<=25:
                    print ' Broken\n----'
                elif qiii==100:
                    print ' GOLDEN\n----'
            else:
                print "Secondary!"
                qiii=choice(range(1,101))
                if qiii>=75:
                    print ' New\n----'
                elif qiii>25 and qiii<75:
                    print ' Used\n----'
                elif qiii<=25:
                    print ' Broken\n----'
                elif qiii==100:
                    print ' GOLDEN\n----'
        elif qiii<50:
            print "----\nARMOR:"
            ss=choice(range(1,5))

            if ss==1:
                print "Headwear"
            elif ss==2:
                print "Chestwear"
            elif ss==3:
                print "Legwear"
            else:
                print "Footwear"

            qiii=choice(range(1,101))
            if qiii>=75:
                print ' New\n----'
            elif qiii>25 and qiii<75:
                print ' Used\n----'
            elif qiii<=25:
                print ' Broken\n----'
            elif qiii==100:
                print ' GOLDEN\n----'



    #Add-ons, mejoras y efectos
    elif p <= 25:
        print "----\nADD-ON:"
        qii=choice(range(1,101))
        if qii>=66:
            pporss=choice(range(1,3))
            if pporss==1:
                print ' for primary weapon!'

                qiiwbuff=choice(range(1,5))
                if qiiwbuff==1:
                    print " +ATK"
                elif qiiwbuff==2:
                    print " +HP"
                elif qiiwbuff==3:
                    print " +DEF"
                elif qiiwbuff==4:
                    print " +SP"

                qiiqw=choice(range(1,3))
                if qiiqw==1:
                    print ' Used\n----'
                elif qiiqw==2:
                    print ' Broken\n----'
            else:
                print ' for secondaty weapon!'

                qiiwbuff=choice(range(1,5))
                if qiiwbuff==1:
                    print " +ATK"
                elif qiiwbuff==2:
                    print " +HP"
                elif qiiwbuff==3:
                    print " +DEF"
                elif qiiwbuff==4:
                    print " +SP"

                qiiqw=choice(range(1,3))
                if qiiqw==1:
                    print ' Used\n----'
                elif qiiqw==2:
                    print ' Broken\n----'
        elif qii>33 and qii<66:
            print ' for User'
            qiipbuff=choice(range(1,5))
            if qiipbuff==1:
                print " +ATK"
            elif qiipbuff==2:
                print " +HP"
            elif qiipbuff==3:
                print " +DEF"
            elif qiipbuff==4:
                print " +SP"
            qiiqp=choice(range(1,3))
            if qiiqp==1:
                print ' Used\n----'
            elif qiiqp==2:
                print ' Broken\n----'
        elif qii<=33:
            print ' for Armor'
            sss=choice(range(1,5))

            if sss==1:
                print "Headwear"
            elif sss==2:
                print "Chestwear"
            elif sss==3:
                print "Legwear"
            else:
                print "Footwear"

            qiiabuff=choice(range(1,5))
            if qiiabuff==1:
                print " +ATK"
            elif qiiabuff==2:
                print " +HP"
            elif qiiabuff==3:
                print " +DEF"
            elif qiiabuff==4:
                print " +SP"
            qiiqa=choice(range(1,3))
            if qiiqa==1:
                print ' Used\n----'
            elif qiiqa==2:
                print ' Broken\n----'
        elif qii==100:
            print 'RARE '
            radd=choice(range(1,3))
            if radd>=1:
                print ' for Weapon\n----'
                qiiwrarebuff=choice(range(1,5))
                qiiwrarebuff=choice(range(1,5))
                qiiwrarebuff=choice(range(1,5))
                if qiiwrarebuff==1:
                    print " +ATK\n"
                elif qiiwrarebuff==2:
                    print " +HP\n"
                elif qiiwrarebuff==3:
                    print " +DEF\n"
                elif qiiwrarebuff==4:
                    print " +SP\n"

            elif radd>2:
                print ' for User\n----'
                qiiurarebuff=choice(range(1,5))
                qiiurarebuff=choice(range(1,5))
                qiiurarebuff=choice(range(1,5))
                if qiiurarebuff==1:
                    print " +ATK\n"
                elif qiiurarebuff==2:
                    print " +HP\n"
                elif qiiurarebuff==3:
                    print " +DEF\n"
                elif qiiurarebuff==4:
                    print " +SP\n"
            elif radd<=3:
                print ' for Armor\n----'
                qiiararebuff=choice(range(1,5))
                qiiararebuff=choice(range(1,5))
                qiiararebuff=choice(range(1,5))
                if qiiararebuff==1:
                    print " +ATK\n"
                elif qiiararebuff==2:
                    print " +HP\n"
                elif qiiararebuff==3:
                    print " +DEF\n"
                elif qiiararebuff==4:
                    print " +SP\n"


    #General Loot: HP+, SP+, Mejoras, Parches ,etc.
    elif p <= 50:
        print "----\nLOOT:"
        qi=choice(range(1,101))
        if qi>=85:
            print ' +HP Item\n----'
        elif qi>15 and qi<85:
            #Materiales
            material=choice(range(1,101))
            if material>=75:
                print ' +HP Ingredients\n----'
            elif material>25 and material<75:
                print ' Scrap\n----'
            elif material<=25:
                print '+SP Ingredients\n----'
            elif material==100:
                print ' CHIP ELEMENTAL\n----'
        elif qi<=15:
            print ' +SP Item\n----'
        elif qi==100:
            print ' REVIVE\n----'
    elif p>50:
        print "\n\nNothing useful here...\n"

#TK STUFF

w1 = Tk()
w1.geometry("295x350")
"""w1.config(bg="black")"""
welcome = Label(w1, text="Select an event!",).grid(row=0, column=0, sticky=N)
#AI TK

player_menu = Label(w1, text="\nPLAYER:",).grid(row=1, column=0 ,sticky=N)
player_hit_chance = Button(w1, text =" \n  Attack!  \n",command=player_hit_chance,bd=2).grid(row=1, column=1, sticky=N)

foe_menu = Label(w1, text="\nENEMY:",).grid(row=2, column=0 ,sticky=N)
foe_common_ai = Button(w1, text =" \n  Regular  \n",command=foe_common_ai,bd=2).grid(row=2, column=1, sticky=N)
foe_pk_ai = Button(w1, text =" \n      PSI      \n",command=foe_pk_ai,bd=2).grid(row=2, column=2, sticky=N)



#DICE TK

chance_menu = Label(w1, text="CHANCE:",).grid(row=3, column=0 ,sticky=N)

coin_toss = Button(w1, text =" \n    Coin    \n",command=coin_toss,bd=4).grid(row=4, column=0 ,sticky=N)
dado4 = Button(w1, text =" \n      4       \n",command=dado4,bd=4).grid(row=4, column=1 ,sticky=N)
dado6 = Button(w1, text =" \n      6       \n",command=dado6,bd=4).grid(row=4, column=2 ,sticky=N)
dado8 = Button(w1, text =" \n      8       \n ",command=dado8,bd=4).grid(row=4, column=3 ,sticky=N)
dado10 = Button(w1, text =" \n      10      \n ",command=dado10,bd=4).grid(row=5, column=0 ,sticky=N)
dado12 = Button(w1, text =" \n      12      \n ",command=dado12,bd=4).grid(row=5, column=1 ,sticky=N)
dado20 = Button(w1, text =" \n      20      \n ",command=dado20,bd=4).grid(row=5, column=2 ,sticky=N)
dado100 = Button(w1, text =" \n    100     \n ",command=dado100,bd=4).grid(row=5, column=3 ,sticky=N)

#LOOT_TK

loot_menu = Label(w1, text="\nLOOT:",).grid(row=6, column=0 ,sticky=N)
loot_chance = Button(w1, text =" \n      Get!     \n", command=loot_chance ,bd=5).grid(row=6, column=1)

#



w1.mainloop()


