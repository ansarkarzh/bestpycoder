heights = list(map(int, input().split()))
maxim = max(heights) + 1
while 1:
    if (sum(heights) + maxim) / 7 % 1 == 0:
        print(maxim)
        break
    else:
        maxim += 1