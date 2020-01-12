import sys
class Queue:

    def __init__(self):
        self.lst=[]

    def push(self, x):
        self.lst.append(x)
    def pop(self):
        if len(self.lst)!=0:
            print(self.lst.pop(0))
        else:
            print('-1')
    def size(self):
        print(len(self.lst))
    def empty(self):
        if len(self.lst)==0:
            print('1')
        else:
            print('0')
    def front(self):
        if len(self.lst)!=0:
            print(self.lst[0])
        else:
            print('-1')
    def back(self):
        if len(self.lst)!=0:
            print(self.lst[-1])
        else:
            print('-1')


n=int(input())
q1=Queue()
for i in range(n):
    a=sys.stdin.readline().split()
    if len(a)>1:
        q1.push(int(a[-1]))
    elif a[0]=='pop':
        q1.pop()
    elif a[0]=='size':
        q1.size()
    elif a[0]=='empty':
        q1.empty()
    elif a[0]=='front':
        q1.front()
    elif a[0]=='back':
        q1.back()
