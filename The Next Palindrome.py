n = int(input())
for i in range(n):
    numstr = input()
    numint = int(numstr)
    while numstr[:-1] != numstr:
        numint += 1
        numstr = str(numint)
    else:
        print(numstr)
