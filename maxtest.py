num = 1
add = 2
count = 0
while count < 501:
    num += add
    add += 1
    for x in range(1, num):
        if num % x == 0:
            count += 1
            break
    if count > 500:
        print(num)
    count = 0
# oder 13 machen, also mal schaeun worauf du bock hast hihi