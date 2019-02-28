n = int(input())
out = []
while n != -1:
    i = 1
    values = [1]
    value = -1
    while value < n:
        value = values[i-1] + 6*i
        values.append(value)
        i += 1
    if n == 1:
        out.append('Y')
    elif values[-1] == n:
        out.append('Y')
    else:
        out.append('N')
    n = int(input())
for i in range(len(out)):
    print(out[i])
        
  
