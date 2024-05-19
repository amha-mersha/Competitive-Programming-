n = int(input())
nums = list(map(int, input().split()))
state_one = (0,nums[0])
state_two = (abs(nums[1]-nums[0]), nums[1])
for i in range(2, n):
    temporary = state_one
    state_one = state_two
    state_two = (min(temporary[0] + abs(nums[i]-temporary[1]), state_two[0] + abs(nums[i]-state_two[1])), nums[i])
print(state_two[0])
