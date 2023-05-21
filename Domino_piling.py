def Domino(c,r):
    if c%2 == 0 and r%2 == 0:
        n = int(max(c,r) / 2)
        return n * min(c,r)
    elif c%2 == 1 and r%2 == 1:
        n = int((max(c,r)-1)/2)
        m = int((min(c,r)-1)/2)
        return n*min(c,r) + m
    elif c%2 == 0:
        return int(c/2) * r 
    else:
        return int(r/2) * c


c,r = input().split()
c= int(c)
r = int(r)
print(Domino(c,r))
