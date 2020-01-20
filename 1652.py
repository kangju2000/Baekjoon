import sys
n=int(input())
lst=[]
for _ in range(n):
    lst.append(sys.stdin.readline().rstrip())

r=0
c=0
for i in range(n):
    cnt=0
    for j in range(n):
        if lst[i][j]!='.':
            if cnt>=2:
                r+=1
            cnt=0
        else:
            cnt+=1
    if cnt>=2:
        r+=1

for i in range(n):
    cnt=0
    for j in range(n):
        if lst[j][i]!='.':
            if cnt >= 2:
                c += 1
            cnt=0
        else:
            cnt+=1
    if cnt>=2:
        c+=1
print(r,c)