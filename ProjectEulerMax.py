import math


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


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
    number = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450 "
    sum = 0
    for x in range(len(number) - 13):
        num = number[x:x + 13]
        test = 1
        for i in range(len(num)):
            test = test * int(num[i])
        if test > sum:
            sum = test
    print(sum)


def prob9():
    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, 1000):
                if a * a + b * b == c * c and a + b + c == 1000:
                    if a * b * c > 0:
                        print(a * b * c)
                        a = 1000
                        b = 1000
                        c = 1000


def prob10():
    sum = 17
    for x in range(9, 2000000, 2):
        if is_prime(x):
            sum += x
    print(sum)
