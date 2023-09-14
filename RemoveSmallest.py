res = []
for i in range(int(input())):
    n = int(input())
    nums = sorted(list(map(int,input().split())))
    cond = True
    for i in range(n-1):
        if nums[i]+1 < nums[i+1]:
            cond = False
            break
    if cond:
        res.append("YES")
    else:
        res.append("NO")
for i in res:
    print(i)
