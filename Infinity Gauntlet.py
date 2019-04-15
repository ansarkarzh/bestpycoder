stones = {'purple': 'Power', 'green': 'Time', 'blue': 'Space', 'orange': 'Soul', 'red': 'Reality', 'yellow': 'Mind'}
n = int(input())
a = []
for i in range(n):
    a.append(input())
    if stones[a[-1]]:
        stones.pop(a[-1])
print(len(stones))
for i in stones:
    print(stones[i])