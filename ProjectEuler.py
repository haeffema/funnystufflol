import math


def prob1():
    sum = 0
    for x in range(1000):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    print("Problem 1: " + str(sum))


def prob2():
    sum = 0
    first = 1
    second = 2
    while first <= 4000000:
        if second % 2 == 0:
            sum += second
        zw = first + second
        first = second
        second = zw
    print("Problem 2: " + str(sum))


def prob3():
    sum = 600851475143
    test = 2
    while test * test < sum:
        while sum % test == 0:
            sum = sum / test
        test = test + 1
    print("Problem 3: " + str(sum))


def prob4():
    sum = 0
    for first in range(100, 1000):
        for second in range(100, 1000):
            num = first * second
            num2 = (num % 10) * 100000
            num2 += math.floor(num % 100 / 10) * 10000
            num2 += math.floor(num % 1000 / 100) * 1000
            num2 += math.floor(num % 10000 / 1000) * 100
            num2 += math.floor(num % 100000 / 10000) * 10
            num2 += math.floor(num % 1000000 / 100000)
            if num == num2 and sum < num:
                sum = num
    print(sum)


def prob5():
    num = 2520
    sum = num
    test = 0
    while num == 2520:
        for i in range(1, 21):
            test += sum % i
        if test == 0:
            num = sum
        else:
            test = 0
            sum += 20
    print(num)


def prob6():
    first = 0
    second = 0
    for x in range(1, 101):
        first += x
        second += x * x
    first = first * first
    sum = first - second
    print(sum)


def prob7():
    count = 6
    prime = 13
    x = prime
    while count < 10001:
        x += 2
        test = True
        for i in range(2, x):
            if x % i == 0:
                test = False
        if test:
            prime = x
            count += 1
    print(prime)


def prob8():
    pass