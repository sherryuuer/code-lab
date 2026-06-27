class FootballPlayer:
    # class object attribute
    membership = True

    def __init__(self, name, age):
        # attribute of instance
        self.name = name
        self.age = age

    def shot(self):
        return f"My name is {self.name}!"

    @classmethod
    def add_member(cls, name, age):
        if cls.membership:
            return cls(name, age)

    @staticmethod
    def add_number(num):
        return num


player1 = FootballPlayer("Sally", 17)
print(player1)
player2 = FootballPlayer.add_member("Cody", 34)
print(player2)

# >line1   SyntaxError: invalid syntax
# why?
