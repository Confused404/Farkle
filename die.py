import random

class Die:
    number = 0
    special = False
    value = 0 

    def __init__(self):
        self.number = random.randint(1, 6)
        self.special = self.special_check()
        self.value = self.get_value()

    def special_check(self):
        if self.number == 1 or self.number == 5:
            #print("It is either a 1 or a 5")
            return True
        else:
            #print("It is not a 1 or 5")
            return False

    def get_value(self):
        if self.number == 5:
            return 50
        else:
            return 100

    