import sys
import random


start = int(sys.argv[1])
end = int(sys.argv[2])
random_num = random.choice(list(range(start, end)))
print(random_num)

while True:
    try:
        guess = input("OK, guess the number!: ")
        if int(guess) < start or int(guess) > end:
            print(f"Hey You made it {start} to {end}. Remember?")
            continue
        elif int(guess) == random_num:
            print("YOU WIN!")
            break
        else:
            print("Try again!")
            continue
    except ValueError:
        print("Please enter a numebr.")
        continue
