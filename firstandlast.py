n=input()
for i in xrange(n):
    a=input()
    count = 0
    first=a%10
    while a>=1:
        if a/10 < 1:
            second = a
        a /= 10
    print first + second
