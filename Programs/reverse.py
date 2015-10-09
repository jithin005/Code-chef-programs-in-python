n=input()
for i in xrange(n):
    a=input()
    count = 0
    while a>=1:
        count =(count*10)+a%10
        a /= 10
    print count
