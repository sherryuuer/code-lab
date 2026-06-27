import random


def run_guess(guess, answer):
    try:
        if 0 < guess < 11:
            if guess == answer:
                return "You are a genius!"
        else:
            return "Hey bozo, I said 1~10."
    except TypeError:
        return TypeError


if __name__ == '__main__':
    # 提高代码复用性，只有执行本文件才会被执行，被调用为模块的时候不会被执行
    answer = random.randint(1, 10)
    print(answer)
    while True:
        try:
            guess = int(input("Guess a number 1~10: "))
            res = run_guess(guess, answer)
            if res:
                print(res)
                break
        except ValueError:
            print("Please enter a numebr.")
            continue
