import helper
class Bani:
    def __init__(self, total, bet):
        if helper.isInt(total):
            self.__total = total
        else:
            raise ValueError("baiatu tre sa pui numere!")
        if helper.isInt(bet):
            self.__bet = bet
        else:
            raise ValueError("baiatu numere te rog!")

    # Getters
    def getTotal(self):
        return self.__total

    def getBet(self):
        return self.__bet

    # Setters
    def setTotal(self, newTotal):
        if helper.isInt(newTotal):
            self.__total = newTotal
        else:
            raise ValueError("baiatu tre sa pui numere!")

    def setBet(self, newBet):
        if helper.isInt(newBet):
            self.__bet = newBet
        else:
            raise ValueError("baiatu numere te rog!")

    def __repr__(self):
        return "\tTotal: " + str(self.__total) + "\n \tCurrent bet: " + str(self.__bet)