a=input()
for i in range(len(a)):
    if a[i].isalpha():
        k=ord(a[i])+13
        if a[i].isupper():
            if k>ord('Z'):
                k-=26
        elif a[i].islower():
            if k>ord('z'):
                k-=26
        print(chr(k), end='')
    else:
        print(a[i], end='')
