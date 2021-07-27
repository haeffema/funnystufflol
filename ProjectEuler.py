# macht des, ist geil :)
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
        zw = first+second
        first = second
        second = zw
    print("Problem 2: " + str(sum))

def prob3():
