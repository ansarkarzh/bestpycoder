n = []
a=[]
oexist = 0
while 1:
    test = input()
    if test == '0':
        break
    else:
        n.append(test)
for i in range(len(n)):
    a.append([])
    for j in range(int(n[i])+1):
        lololo = list(str(j))
        for s in range(len(lololo)):
            if lololo[s] == '0' and j<10:
                continue
            else:
                a[i].append(int(lololo[s]))
for i in range(len(n)):
    for j in range(1, len(a[i]), 2):
        a[i][j] = a[i][j] - a[i][j] - a[i][j]
    print(sum(a[i]))