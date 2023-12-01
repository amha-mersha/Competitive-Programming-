class Solution(object):
    def romanToInt(self, s):
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        arabian = 0
        if len(s) == 1:
            return roman[s[0]]
        counted = False
        for i in range(1,len(s)+1):
            if s[i-1:i+1] in ["IV","IX","XL","XC","CD","CM"]:
                arabian += (roman[s[i]]-roman[s[i-1]])
                counted = True
            elif not counted:
                arabian += roman[s[i-1]]
            else:
                counted = False
        return arabian 


