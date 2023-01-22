def isInt(value):
    if int(value) == value:
        return True
    return False
def fullLineWin(result1, result2, result3, bani, total):
    if result1 == ['🐉', '🐉', '🐉', '🐉', '🐉'] or result2 == ['🐉', '🐉', '🐉', '🐉', '🐉'] or result3 == ['🐉', '🐉', '🐉', '🐉',
                                                                                                   '🐉']:
        print("🐉 BINE BOSSSS!! Dragonasu' meu preferat 🐉")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 16
        bani.setTotal(total)
    elif result1 == ['👺', '👺', '👺', '👺', '👺'] or result2 == ['👺', '👺', '👺', '👺', '👺'] or result3 == ['👺', '👺', '👺', '👺',
                                                                                                     '👺']:
        print("👺 BINE BOSSSS!! Mascatu' mascatilor 👺")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 14
        bani.setTotal(total)
    elif result1 == ['🐧️', '🐧️', '🐧️', '🐧️', '🐧️'] or result2 == ['🐧️', '🐧️', '🐧️', '🐧️', '🐧️'] or result3 == ['🐧️',
                                                                                                               '🐧️',
                                                                                                               '🐧️',
                                                                                                               '🐧️',
                                                                                                               '🐧️']:
        print("🐧 BINE BOSSSS!! Si cu pinguinii in Antarctica castigi 🐧")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 18
        bani.setTotal(total)
    elif result1 == ['💥', '💥', '💥', '💥', '💥'] or result2 == ['💥', '💥', '💥', '💥', '💥'] or result3 == ['💥', '💥', '💥', '💥',
                                                                                                     '💥']:
        print("💥 BINE BOSSSS!! Bombardezi tot pe aici 💥")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 12
        bani.setTotal(total)
    elif result1 == ['💲', '💲', '💲', '💲', '💲'] or result2 == ['💲', '💲', '💲', '💲', '💲'] or result3 == ['💲', '💲', '💲', '💲',
                                                                                                     '💲']:
        print("😎 BINE BOSSSS!! De banii asta iti iei yacht ce sa mai 😎")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 20
        bani.setTotal(total)

def fourInALineWin(result1, result2, result3, bani, total):
    if (result1[0] == result1[1] == result1[2] == result1[3] == '🐉') or (
            result2[0] == result2[1] == result2[2] == result2[3] == '🐉') or (
            result3[0] == result3[1] == result3[2] == result3[3] == '🐉'):
        print("🐉 BINE BOSSSS!! Dragonasu' meu preferat 🐉")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 8
        bani.setTotal(total)
    elif (result1[0] == result1[1] == result1[2] == result1[3] == '👺') or (
            result2[0] == result2[1] == result2[2] == result2[3] == '👺') or (
            result3[0] == result3[1] == result3[2] == result3[3] == '👺'):
        print("👺 BINE BOSSSS!! Mascatu' mascatilor 👺")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 7
        bani.setTotal(total)
    elif (result1[0] == result1[1] == result1[2] == result1[3] == '🐧️') or (
            result2[0] == result2[1] == result2[2] == result2[3] == '🐧️') or (
            result3[0] == result3[1] == result3[2] == result3[3] == '🐧️'):
        print("🐧 BINE BOSSSS!! Si cu pinguinii in Antarctica castigi 🐧")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 9
        bani.setTotal(total)
    elif (result1[0] == result1[1] == result1[2] == result1[3] == '💥') or (
            result2[0] == result2[1] == result2[2] == result2[3] == '💥') or (
            result3[0] == result3[1] == result3[2] == result3[3] == '💥'):
        print("💥 BINE BOSSSS!! Bombardezi tot pe aici 💥")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 6
        bani.setTotal(total)
    elif (result1[0] == result1[1] == result1[2] == result1[3] == '💲') or (
            result2[0] == result2[1] == result2[2] == result2[3] == '💲') or (
            result3[0] == result3[1] == result3[2] == result3[3] == '💲'):
        print("😎 BINE BOSSSS!! De banii asta iti iei yacht ce sa mai 😎")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 10
        bani.setTotal(total)

def threeInALineWin(result1, result2, result3, bani, total):
    if (result1[0] == result1[1] == result1[2] == '🐉') or (
            result2[0] == result2[1] == result2[2] == '🐉') or (
            result3[0] == result3[1] == result3[2] == '🐉'):
        print("🐉 BINE BOSSSS!! Dragonasu' meu preferat 🐉")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 4
        bani.setTotal(total)
    elif (result1[0] == result1[1] == result1[2] == '👺') or (
            result2[0] == result2[1] == result2[2] == '👺') or (
            result3[0] == result3[1] == result3[2] == '👺'):
        print("👺 BINE BOSSSS!! Mascatu' mascatilor 👺")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 3
        bani.setTotal(total)
    elif (result1[0] == result1[1] == result1[2] == '🐧️') or (
            result2[0] == result2[1] == result2[2] == '🐧️') or (
            result3[0] == result3[1] == result3[2] == '🐧️'):
        print("🐧 BINE BOSSSS!! Si cu pinguinii in Antarctica castigi 🐧")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 4
        bani.setTotal(total)
    elif (result1[0] == result1[1] == result1[2] == '💥') or (
            result2[0] == result2[1] == result2[2] == '💥') or (
            result3[0] == result3[1] == result3[2] == '💥'):
        print("💥 BINE BOSSSS!! Bombardezi tot pe aici 💥")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 3
        bani.setTotal(total)
    elif (result1[0] == result1[1] == result1[2] == '💲') or (
            result2[0] == result2[1] == result2[2] == '💲') or (
            result3[0] == result3[1] == result3[2] == '💲'):
        print("😎 BINE BOSSSS!! De banii asta iti iei yacht ce sa mai 😎")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 5
        bani.setTotal(total)

def fullDiagonalWin1(result1, result2, result3, bani, total):
    if result1[0] == result2[1] == result3[2] == result2[3] == result1[4] == '🐉':
        print("🐉 BINE BOSSSS!! Dragonasu' meu preferat 🐉")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 16
        bani.setTotal(total)
    elif result1[0] == result2[1] == result3[2] == result2[3] == result1[4] == '👺':
        print("👺 BINE BOSSSS!! Mascatu' mascatilor 👺")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 14
        bani.setTotal(total)
    elif result1[0] == result2[1] == result3[2] == result2[3] == result1[4] == '🐧️':
        print("🐧 BINE BOSSSS!! Si cu pinguinii in Antarctica castigi 🐧")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 18
        bani.setTotal(total)
    elif result1[0] == result2[1] == result3[2] == result2[3] == result1[4] == '💥':
        print("💥 BINE BOSSSS!! Bombardezi tot pe aici 💥")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 12
        bani.setTotal(total)
    elif result1[0] == result2[1] == result3[2] == result2[3] == result1[4] == '💲':
        print("😎 BINE BOSSSS!! De banii asta iti iei yacht ce sa mai 😎")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 20
        bani.setTotal(total)

def fullDiagonalWin2(result1, result2, result3, bani, total):
    if result3[0] == result2[1] == result1[2] == result2[3] == result3[4] == '🐉':
        print("🐉 BINE BOSSSS!! Dragonasu' meu preferat 🐉")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 16
        bani.setTotal(total)
    elif result3[0] == result2[1] == result1[2] == result2[3] == result3[4] == '👺':
        print("👺 BINE BOSSSS!! Mascatu' mascatilor 👺")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 14
        bani.setTotal(total)
    elif result3[0] == result2[1] == result1[2] == result2[3] == result3[4] == '🐧️':
        print("🐧 BINE BOSSSS!! Si cu pinguinii in Antarctica castigi 🐧")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 18
        bani.setTotal(total)
    elif result3[0] == result2[1] == result1[2] == result2[3] == result3[4] == '💥':
        print("💥 BINE BOSSSS!! Bombardezi tot pe aici 💥")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 12
        bani.setTotal(total)
    elif result3[0] == result2[1] == result1[2] == result2[3] == result3[4] == '💲':
        print("😎 BINE BOSSSS!! De banii asta iti iei yacht ce sa mai 😎")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 20
        bani.setTotal(total)

def fourDiagonalWin(result1, result2, result3, bani, total):
    if result1[0] == result2[1] == result3[2] == result2[3] == '🐉':
        print("🐉 BINE BOSSSS!! Dragonasu' meu preferat 🐉")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 8
        bani.setTotal(total)
    elif result1[0] == result2[1] == result3[2] == result2[3] == '👺':
        print("👺 BINE BOSSSS!! Mascatu' mascatilor 👺")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 7
        bani.setTotal(total)
    elif result1[0] == result2[1] == result3[2] == result2[3] == '🐧️':
        print("🐧 BINE BOSSSS!! Si cu pinguinii in Antarctica castigi 🐧")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 9
        bani.setTotal(total)
    elif result1[0] == result2[1] == result3[2] == result2[3] == '💥':
        print("💥 BINE BOSSSS!! Bombardezi tot pe aici 💥")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 6
        bani.setTotal(total)
    elif result1[0] == result2[1] == result3[2] == result2[3] == '💲':
        print("😎 BINE BOSSSS!! De banii asta iti iei yacht ce sa mai 😎")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 10
        bani.setTotal(total)

def threeDiagonalWin(result1, result2, result3, bani, total):
    if result1[0] == result2[1] == result3[2] == '🐉':
        print("🐉 BINE BOSSSS!! Dragonasu' meu preferat 🐉")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 4
        bani.setTotal(total)
    elif result1[0] == result2[1] == result3[2] == '👺':
        print("👺 BINE BOSSSS!! Mascatu' mascatilor 👺")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 3
        bani.setTotal(total)
    elif result1[0] == result2[1] == result3[2] == '🐧️':
        print("🐧 BINE BOSSSS!! Si cu pinguinii in Antarctica castigi 🐧")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 4
        bani.setTotal(total)
    elif result1[0] == result2[1] == result3[2] == '💥':
        print("💥 BINE BOSSSS!! Bombardezi tot pe aici 💥")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 3
        bani.setTotal(total)
    elif result1[0] == result2[1] == result3[2] == '💲':
        print("😎 BINE BOSSSS!! De banii asta iti iei yacht ce sa mai 😎")
        print()
        if bani.getTotal() == 0:
            total = bani.getBet()
        total += bani.getBet() * 5
        bani.setTotal(total)

def allWins(result1, result2, result3, bani, total):
    fullLineWin(result1, result2, result3, bani, total)
    fullDiagonalWin1(result1, result2, result3, bani, total)
    fullDiagonalWin2(result1, result2, result3, bani, total)
    fourInALineWin(result1, result2, result3, bani, total)
    fourDiagonalWin(result1, result2, result3, bani, total)
    threeInALineWin(result1, result2, result3, bani, total)
    threeDiagonalWin(result1, result2, result3, bani, total)