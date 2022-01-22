'''
2.2 Feladat
Írj egy programot, amely létrehoz egy 'tarolo' nevű listát, amelynek a három listaeleme egy-egy három elemű lista! 
Ezen beágyazott listák elemei legyenek sztring formátumban: 'O '. 
A program járja be a listákat, és jelenítse meg a bennük tárolt értékeket úgy, hogy azok egy 3x3-as rácsot adjanak ki. 
A rács képernyőn való megjelenítéséről egy eljárás gondoskodjon!

    O O O
    O O O
    O O O 
  
Feladat
Egészítsd ki úgy a programot, hogy a felhasználó megadhasson egy koordinátát (a bal felső rácspont koordinátája (0;0), a jobb alsó pedig (2;2)), és ekkor a program rajzolja ki úgy a 3x3-as rácsot, hogy a megadott koordinátán 'O ' helyett, '+ ' legyen!
'''

tarolo = []
fuggoleges =int(input('adj szamot(0-2)'))
if fuggoleges > 2:
    fuggoleges = 1 
    print('a megadott szam nagyobb mint 2 \n Az alapertelmezett szamra lett allitva (1)')
vizszintes =int(input('adj szamot(0-2)'))
if vizszintes > 2:
    vizszintes = 1 
    print('a megadott szam nagyobb mint 2 \n Az alapertelmezett szamra lett allitva (1)')

for i in range(3):
   tarolo.append(['O ' for szam in range(3)])

tarolo[fuggoleges][vizszintes] = tarolo[fuggoleges][vizszintes].replace('O ', '+ ')


def listToString(i): 
    str1 = " " 
    return (str1.join(i))

def ooo():
    for i in tarolo:
        print(listToString(i))
ooo()