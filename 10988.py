a=input()
L=len(a)
if L%2==0:
    for i in range(int(L/2)):
        if a[i]!=a[L-i-1]:
            print(0)
            exit(0)
else:
    for i in range(L//2):
        if a[i]!=a[L-i-1]:
            print(0)
            exit(0)
print(1)
