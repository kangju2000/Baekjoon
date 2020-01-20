import sys
while True:
    stk=[]
    a=sys.stdin.readline().rstrip()
    if  a=='.':
        exit(0)
    for i in range(len(a)):
        if a[i]=='(' or a[i]=='[':
            stk.append(a[i])

        elif a[i]==')':
            if len(stk)==0:
                stk.append(a[i])
                break
            if stk[-1]=='(':
                stk.pop()
            else:
                break

        elif a[i]==']':
            if len(stk)==0:
                stk.append(a[i])
                break
            if stk[-1]=='[':
                stk.pop()
            else:
                break
    if len(stk)==0:
        print('yes')
    else:
        print('no')
