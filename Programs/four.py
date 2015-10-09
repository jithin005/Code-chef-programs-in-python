
n=input()
for i in xrange(n):
    a=input()
    count = 0
    while a>=1:
        if a%10==4:
            count+=1
        a /= 10
    print count