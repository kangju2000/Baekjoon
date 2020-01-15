import sys
# d=0(북) 1(동) 2(남) 3(서)        0
#                               3    1
#                                 2
n,m=map(int,sys.stdin.readline().split())
r,c,d=map(int,sys.stdin.readline().split())
room=[]
for i in range(n):
    room[i] = list(map(int, input().split()))

done=1
while True:
    if d==0: #북쪽
        if c-1>=0: #왼쪽에 무언가가 있을 때
            if room[r][c-1]
