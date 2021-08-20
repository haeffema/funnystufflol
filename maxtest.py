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