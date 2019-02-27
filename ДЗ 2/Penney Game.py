p = int(input())
out = []
for i in range(p):
    ttt = 0
    tth = 0
    tht = 0
    thh = 0
    htt = 0
    hth = 0
    hht = 0
    hhh = 0
    n = int(input())
    a = input()
    for j in range(len(a)-2):
        sequence = a[j] + a[j+1] + a[j+2]
        if sequence == 'TTT':
            ttt += 1
        elif sequence == 'TTH':
            tth += 1
        elif sequence == 'THT':
            tht += 1
        elif sequence == 'THH':
            thh += 1
        elif sequence == 'HTT':
            htt += 1
        elif sequence == 'HTH':
            hth += 1
        elif sequence == 'HHT':
            hht += 1
        elif sequence == 'HHH':
            hhh += 1
    out.append([])
    out[n-1] = [n, ttt, tth, tht, thh, htt, hth, hht, hhh]
for i in range(p):
    print (*out[i], sep = ' ')