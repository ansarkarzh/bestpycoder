word = input()
lena = len(word)
hops = []
a, b = 1, 1
while a < lena + 1:
    hops.append(word[a-1])
    a, b = b, a+b
hops.pop(0)
print(''.join(hops))