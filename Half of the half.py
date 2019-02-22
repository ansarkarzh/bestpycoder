n=int(input())
l=[]
for i in range(n):
    l.append(list(input()))
    leng=len(l[i])//2
    del l[i][leng:]
    print(''.join(l[i][::2]))
