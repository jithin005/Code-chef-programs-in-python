n=input()
for i in xrange(n):
    b=[]
    a=raw_input().split()
    for j in range(len(a)):
        b.append(int(a[j]))
    b.sort()
    print b[len(a)-2]

