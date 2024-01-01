class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return num
        isNeg,count = False,0,
        if num < 0:
            num = str(num)[1:]
            isNeg = True
        else:
            num = str(num)
        nums = []
        for i in num:
            if i != '0':
                nums.append(i)
            else:
                count += 1
        nums.sort(reverse = isNeg)
        if isNeg:
            return -1*int("".join(nums)+"0"*count)
        nums.insert(1,"0"*count)
        return int("".join(nums))