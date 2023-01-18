import random

def printMenu():
    msg = "\t 💲💲💲💲💲💲💲💲 \n"
    msg += "\t 🤩 PACANEA 🤩 \n"
    msg += "\t Linie completa castiga \n"
    msg += "\t 1 - Joci? Stiu ca vrei 😏 \n"
    msg += "\t 2 - Iesi din joc? Bine ca esti responsabil 🙄 \n"
    msg += "\t 💲💲💲💲💲💲💲💲 \n"
    print(msg)

def pacanea():
    stop = True
    while stop == True:
        try:
            printMenu()
            option = int(input("💸 Alege boss, 1 sau 2: "))
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
                elif result1 == ['👺','👺','👺','👺','👺'] or result2 == ['👺','👺','👺','👺','👺'] or result3 == ['👺','👺','👺','👺','👺']:
                    print("👺 BINE BOSSSS!! Mascatu' mascatilor 👺")
                elif result1 == ['🐧️','🐧️','🐧️','🐧️','🐧️'] or result2 == ['🐧️','🐧️','🐧️','🐧️','🐧️'] or result3 == ['🐧️','🐧️','🐧️','🐧️','🐧️']:
                    print("🐧 BINE COAIEEE!! Si cu pinguinii in Antarctica castigi 🐧")
                elif result1 == ['💥','💥','💥','💥','💥'] or result2 == ['💥','💥','💥','💥','💥'] or result3 == ['💥','💥','💥','💥','💥']:
                    print("💥 BINE BOSSSS!! Bombardezi tot pe aici 💥")
                elif result1 == ['💲','💲','💲','💲','💲'] or result2 == ['💲','💲','💲','💲','💲'] or result3 == ['💲','💲','💲','💲','💲']:
                    print("😎 BINE BOSSSS!! De banii asta iti iei yacht ce sa mai 😎")
                else:
                    print("😣 Mai incearca bos. Urmatoarea intra promit 😣")
            elif option == 2:
                print("Responsabilule, ne mai vedem noi 😏")
                stop = False
            else:
                print("1 SAU 2 BAAA, ESTI PROST? 🤥")
        except ValueError:
            print("Esti prost rau smr... 😪")

pacanea()
