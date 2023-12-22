class BodyInfo:
    def __init__(self):
        self.name = None

    @staticmethod
    def bmi(weight, height):
        return weight / (height**2)


weight = 75
height = 1.8
person = BodyInfo()
print(person.name)
print(BodyInfo.bmi(weight, height))
print(person.bmi(weight, height))

# 静态方法没有self也没有cls，不会影响类的变量，只是为了得出结果
