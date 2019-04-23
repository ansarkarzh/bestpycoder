a = input()
hops = []
spaces = 0
for i in range(len(a)):
    aba = ord(a[i])
    if aba >= ord('0') and aba <= ord('9'):
        value = aba-ord('0')
    else:
        value = aba - ord('A') + 10
    value = ((value - (i+1)) % 27 + 27) % 27
    if chr(value + 96) == '`':
        hops.append(' ')
        continue
    else:
        hops.append(chr(value + 96))
print(''.join(hops))