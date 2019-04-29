a = list(map(int, input().split()))
b = list(map(int , input().split()))
counter = len(a)
for i in range(len(a)):
    for j in range(len(a)): 
        if i == j:
            continue
        if a[i] < a[j] and b[i]<b[j]:
            counter -= 1
            break
print(counter)
