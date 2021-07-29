for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            if a*a + b*b == c*c and a+b+c==1000:
                if a*b*c > 0:
                    print(a*b*c)
                    a = 1000
                    b = 1000
                    c = 1000