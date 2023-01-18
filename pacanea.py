import random
from bani import Bani

def printMenu():
    msg = "\t 💲💲💲💲💲💲💲💲 \n"
    msg += "\t 🤩 PACANEA 🤩 \n"
    msg += "\t Linie completa castiga \n"
    msg += "\t 1 - Joci? Stiu ca vrei 😏 \n"
    msg += "\t 2 - Vezi banii 💰 \n"
    msg += "\t 3 - Mai baga bani 🤑\n"
    msg += "\t 4 - Schimba betul 😯\n"
    msg += "\t 5 - Iesi din joc? Bine ca esti responsabil 🙄 \n"
    msg += "\t 💲💲💲💲💲💲💲💲 \n"
    print(msg)

def citesteBani():
    total = int(input("Cati bani total baiatu?\n"))
    bet = int(input("Cati bani pariezi baiatu?\n"))
    try:
        return Bani(total,bet)
    except ValueError as ve:
        print(ve)

def pacanea():
    bani = citesteBani()
    total = bani.getTotal()
    bet = bani.getBet()
    stop = True
    while stop == True:
        try:
            printMenu()
            option = int(input("💸 Alege boss: "))
            if option == 1:
                lst = ['👺','🐉','🐧️','💥','💲']
                result1 = []
                result2 = []
                result3 = []
                while len(result1) <= 4:
                    result1.append(random.choice(lst))
                while len(result2) <= 4:
                    result2.append(random.choice(lst))
                while len(result3) <= 4:
                    result3.append(random.choice(lst))
                print("🤑 *sunete de pacanea* 🤑")
                print(result1)
                print(result2)
                print(result3)
                if result1 == ['🐉','🐉','🐉','🐉','🐉'] or result2 == ['🐉','🐉','🐉','🐉','🐉'] or result3 == ['🐉','🐉','🐉','🐉','🐉']:
                    print("🐉 BINE BOSSSS!! Dragonasu' meu preferat 🐉")
                    total = bani.getTotal() * 7
                    bani.setTotal(total)
                elif result1 == ['👺','👺','👺','👺','👺'] or result2 == ['👺','👺','👺','👺','👺'] or result3 == ['👺','👺','👺','👺','👺']:
                    print("👺 BINE BOSSSS!! Mascatu' mascatilor 👺")
                    total = bani.getTotal() * 5
                    bani.setTotal(total)
                elif result1 == ['🐧️','🐧️','🐧️','🐧️','🐧️'] or result2 == ['🐧️','🐧️','🐧️','🐧️','🐧️'] or result3 == ['🐧️','🐧️','🐧️','🐧️','🐧️']:
                    print("🐧 BINE COAIEEE!! Si cu pinguinii in Antarctica castigi 🐧")
                elif result1 == ['💥','💥','💥','💥','💥'] or result2 == ['💥','💥','💥','💥','💥'] or result3 == ['💥','💥','💥','💥','💥']:
                    print("💥 BINE BOSSSS!! Bombardezi tot pe aici 💥")
                    total = bani.getTotal() * 3
                    bani.setTotal(total)
                elif result1 == ['💲','💲','💲','💲','💲'] or result2 == ['💲','💲','💲','💲','💲'] or result3 == ['💲','💲','💲','💲','💲']:
                    print("😎 BINE BOSSSS!! De banii asta iti iei yacht ce sa mai 😎")
                    total = bani.getTotal() * 10
                    bani.setTotal(total)
                else:
                    print("😣 Mai incearca bos. Urmatoarea intra promit 😣")
                    total = bani.getTotal() - bani.getBet()
                    bani.setTotal(total)
                print("Bani ramasi: \n")
                print(bani)
            elif option == 2:
                print("Ia aici cati bani ai boss: ")
                print(bani)
            elif option == 3:
                newTotal = int(input("Cati bani mai bagi baiatu?\n"))
                newTotal += total
                try:
                    bani.setTotal(newTotal)
                except ValueError as ve:
                    print(ve)
            elif option == 4:
                newBet = int(input("Cat vrei sa pariezi bos?\n"))
                try:
                    bani.setBet(newBet)
                except ValueError as ve:
                    print(ve)
            elif option == 5:
                print("Responsabilule, ne mai vedem noi 😏")
                stop = False
            else:
                print("DE LA 1 LA 5 BAAA, ESTI PROST? 🤥")
        except ValueError:
            print("Esti prost rau smr... 😪")

pacanea()
