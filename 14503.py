import sys
# d=0(북) 1(동) 2(남) 3(서)        0
#                               3    1
# room 0-청소x/1-벽/2-청소o        2
n,m=map(int,sys.stdin.readline().split())
global r, c, d, done, room
r,c,d=map(int,sys.stdin.readline().split())

done=0
room=[]
for i in range(n):
    room.append(list(map(int, sys.stdin.readline().split())))

def rotate():
    global d
    if d==0:
        d=3
    else:
        d-=1
def forward():
    global r, c, d
    if d==0:
        r-=1
    elif d==1:
        c+=1
    elif d==2:
        r+=1
    elif d==3:
        c-=1


def reverse():
    global r,c,d,done,room
    if d==0:
        r+=1
    elif d==1:
        c-=1
    elif d==2:
        r-=1
    elif d==3:
        c+=1

    if room[r][c]==1:
        print(done)
        sys.exit(0)

E=0
while True:
    if room[r][c]==0:
        done+=1
        room[r][c]=2
    if d==0: #북쪽
        if room[r][c-1]==0:
            E=0
            rotate()
            forward()
        elif E==4:
            reverse()
            E=0
        else:
            E+=1
            rotate()
            continue
    elif d==1: #동쪽
        if room[r-1][c]==0:
            E=0
            rotate()
            forward()
        elif E==4:
            reverse()
            E=0
        else:
            E+=1
            rotate()
            continue
    elif d==2: #남쪽
        if room[r][c+1]==0:
            E=0
            rotate()
            forward()
        elif E==4:
            reverse()
            E=0
        else:
            E+=1
            rotate()
            continue
    elif d==3: #서쪽
        if room[r+1][c]==0:
            E=0
            rotate()
            forward()
        elif E==4:
            reverse()
            E=0
        else:
            E+=1
            rotate()
            continue
