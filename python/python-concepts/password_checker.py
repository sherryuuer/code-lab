user_name = input("What's your name: ")
password = input("Input your password: ")

lenth = len(password)
print(f"{user_name}, your password {'*'*lenth} is {lenth} long.")
