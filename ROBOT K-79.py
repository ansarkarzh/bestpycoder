from sys import exit
comms = input()
a = []
coordinates = [0, 0]
n = 1
counter = 0
places = ['00']
for i in comms:
    if i == "S":
        if n == 1:
            coordinates[1] += 1
        elif n == 2:
            coordinates[0] += 1
        elif n == 3:
            coordinates[1] -= 1
        elif n == 4:
            coordinates[0] -= 1
        counter += 1
        x = str(coordinates[0])
        y = str(coordinates[1])
        comp = x + y
        if comp in places:
            print(counter)
            exit()
        else:
            places.append(comp)
    else:
        if i == "R":
            n += 1
        else:
            n -= 1
        if n > 4:
            n = 1
        elif n < 1:
            n = 4
print(-1)