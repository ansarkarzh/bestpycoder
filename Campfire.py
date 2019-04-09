n, m = map(int, input().split())
b = list(map(int, input().split()))
if max(b) > m or sum(b)-n+1<m:
    print('no')
else:
    print('yes')