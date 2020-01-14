import sys
a=sys.stdin.readline().strip()
lst=[]
R=0
for i in range(len(a)):
    if a[i]=='(':
        lst.append(0)
    elif a[i]==')':
        if a[i-1]=='(':
            lst.pop()
            if len(lst) != 0:
                lst[-1]+=1
        else:
            lazor=lst.pop()
            R+=lazor+1
            if len(lst)!=0:
                lst[-1]+=lazor
print(R)
