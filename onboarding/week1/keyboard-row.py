class Solution(object):
    def findWords(self, words):
        res = []
        rows = {}
        for i in "qwertyuiop":
            rows[i] = 1
        for i in "asdfghjkl":
            rows[i] = 2
        for i in "zxcvbnm":
            rows[i] = 3
        for i in words:
            match = True
            for j in range(len(i)-1):
                if rows[i[j].lower()] != rows[i[j+1].lower()]:
                    match = False
                    break
            if match:
                res.append(i)
        return res 



        