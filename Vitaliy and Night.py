n, m = map(int, input().split())
a = []
counter=0
for i in range(n):
    a.append(list(map(int, input().split())))
    for j in range(0, m*2, 2):
       if a[i][j] == 1 or a[i][j+1] == 1:
           counter += 1
print(counter)