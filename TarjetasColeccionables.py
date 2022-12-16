a = int(input())
for i in range(a):
    b, c = input().split(' ')
    b, c = int(b), int(c)
    if b % c == 0:
        print(c)
        break
    else:
        while b % c != 0:
            d = b % c
            b, c = c, d
    print(d)
