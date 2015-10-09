import sys
n=input()
for i in range(n):
    stack=['(']
    top=1
    st=raw_input()
    i=1
    while(top>0 and i<len(st)):
        if(st[i] == '(' or st[i] == '+' or st[i] == '-' or st[i] == '*' or st[i] == '/' or st[i] == '^'):
            stack.append(st[i])
            top += 1
        elif st[i]>='a' and st[i]<='z':
            sys.stdout.write(st[i])
        elif(st[i]==')'):
            if(stack[top-1]!='('):
                sys.stdout.write(stack[top-1])
            top -= 1
        i += 1
    print '\n'