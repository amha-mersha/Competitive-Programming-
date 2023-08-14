class Solution(object):
    def multiply(self, num1, num2):
        sums = 0
        nums = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                sums += (nums[num1[i]] * nums[num2[j]]) * 10**abs(i+j-len(num1)-len(num2)+2)
        return str(sums)

           
