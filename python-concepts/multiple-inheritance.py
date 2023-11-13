class User:
    def login():
        return 'login'


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        return f'attack with {self.power}~'


class Archar(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack_with_arrows(self):
        return f'{self.arrows} arrows used!'

    def attack(self):
        return 'attack with arrows!'

    def run(self):
        return 'run fast!'


class Yoda(Wizard, Archar):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archar.__init__(self, name, arrows)

# archar = Archar("Jack", 20)
# print(archar.attack())


master = Yoda('Sally', power=100, arrows=30)
print(master.attack())
