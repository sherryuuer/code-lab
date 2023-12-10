# for和while后面不要写else。他不代表其他情况而是必定会被执行。

# if there are primes 判断是否是质数对
a = 4
b = 9

# bad practice
for i in range(2, min(a, b) + 1):
    print(f"test {i}")
    if a % i == 0 and b % i == 0:
        print('not coprime')
        break
else:
    print('coprime')


# good practice 1
def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True


print(coprime(a, b))


# good practice 2
def coprime(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime


print(coprime(a, b))
