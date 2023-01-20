import random
from bani import Bani
import helper

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
    print()

def citesteBani():
    total = None
    bet = None
    while total == None or total <= 0:
        try:
            total = int(input("Cati bani total baiatu?\n"))
            if total == 0:
                raise ValueError("ba cum bagi 0 bani???? cum e posibil sa nu bagi bani cand te intreb cat bagi???")
            if total < 0:
                raise ValueError("ba cum ba sa bagi bani cu minus???? esti prost????")
        except ValueError as ve:
            print(ve)
    while bet == None or bet <= 0 or bet > total:
        try:
            bet = int(input("Cati bani pariezi baiatu?\n"))
            if bet == 0:
                raise ValueError("ba cum sa pariezi 0 bani??? stii cum functioneaza o pacanea?????")
            if bet < 0:
                raise ValueError("ba cum ba sa pariezi bani cu minus???? esti prost sau te prefaci????")
            if bet > total:
                raise ValueError("ba tu nu gandesti??? nu poti paria mai mult decat ai!")
        except ValueError as ve:
            print(ve)
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
                    print()
                    total += bani.getBet() * 7
                    bani.setTotal(total)
                elif result1 == ['👺','👺','👺','👺','👺'] or result2 == ['👺','👺','👺','👺','👺'] or result3 == ['👺','👺','👺','👺','👺']:
                    print("👺 BINE BOSSSS!! Mascatu' mascatilor 👺")
                    print()
                    total += bani.getBet() * 5
                    bani.setTotal(total)
                elif result1 == ['🐧️','🐧️','🐧️','🐧️','🐧️'] or result2 == ['🐧️','🐧️','🐧️','🐧️','🐧️'] or result3 == ['🐧️','🐧️','🐧️','🐧️','🐧️']:
                    print("🐧 BINE BOSSSS!! Si cu pinguinii in Antarctica castigi 🐧")
                    total += bani.getBet() * 10
                    bani.setTotal(total)
                elif result1 == ['💥','💥','💥','💥','💥'] or result2 == ['💥','💥','💥','💥','💥'] or result3 == ['💥','💥','💥','💥','💥']:
                    print("💥 BINE BOSSSS!! Bombardezi tot pe aici 💥")
                    print()
                    total += bani.getBet() * 3
                    bani.setTotal(total)
                elif result1 == ['💲','💲','💲','💲','💲'] or result2 == ['💲','💲','💲','💲','💲'] or result3 == ['💲','💲','💲','💲','💲']:
                    print("😎 BINE BOSSSS!! De banii asta iti iei yacht ce sa mai 😎")
                    print()
                    total += bani.getBet() * 20
                    bani.setTotal(total)
                else:
                    print("😣 Mai incearca bos. Urmatoarea intra promit 😣")
                    print()
                    if bani.getTotal() < 0:
                        pass
                    else:
                        total = bani.getTotal() - bani.getBet()
                        bani.setTotal(total)
                if bani.getTotal() < 0:
                    print("Imi pare rau boss da' nu mai ai bani! Ne mai auzim noi, te astept oricand!")
                    print()
                    stop = False
                if bani.getTotal() == 0:
                    print("Vad ca ai ramas pe 0, hai ca iti dau un spin ca is de treaba")
                    print()
                if bani.getTotal() > 0:
                    print("Bani ramasi: \n")
                    print(bani)
                    print()
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
