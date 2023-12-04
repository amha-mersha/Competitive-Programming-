class Solution(object):
    def multiply(self, num1, num2):
        ln = len(num1)+len(num2)
        res = [0]*ln
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                curr = int(num1[i])*int(num2[j])
                curr += res[i+j+1]
                res[i+j+1] = curr%10
                res[i+j] += curr//10
        res_str =  "".join(map(str,res)).lstrip("0")
        return res_str if res_str else "0"

        