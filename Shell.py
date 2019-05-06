n = int(input())
shell = []
man = []
for i in range(n):
    values = list(map(int, input().split()))
    if values[0] == 1:
        shell.insert(0, values[1])
    elif values[0] == 2:
        shell.append(values[1])
    elif values[0] == 3:
        man.append(shell.pop(0))
    else:
        man.append(shell.pop(-1))
print(*man, sep=" ")