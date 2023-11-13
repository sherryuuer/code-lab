# Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
Caro = Cat("Caro", 1)
Sara = Cat("Sara", 1.5)
Dolly = Cat("Dolly", 1)


# 2 Create a function that finds the oldest cat
def find_oidest(cats):
    oldest = cats[0]
    for cat in cats:
        if cat.age > oldest.age:
            oldest = cat

    return oldest


oldest_cat = find_oidest([Caro, Sara, Dolly])
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {oldest_cat.age} years old.")
