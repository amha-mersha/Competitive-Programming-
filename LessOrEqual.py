n,k = map(int, input().split())
nums = sorted(list(map(int, input().split())))
if k == 0 and nums[0]-1 > 0:
    print(nums[0]-1)
elif k == 0 and nums[0]-1<= 0:
    print(-1)
elif k == n:
    print(nums[k-1])
else:
    if nums[k] == nums[k-1]:
        print(-1)
    else:
        print(nums[k-1])
    
