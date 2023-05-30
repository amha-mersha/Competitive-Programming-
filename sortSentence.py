class Solution:
    def sortSentence(self, s):
        
        splited_string = s[::-1].split()
        splited_string.sort()
        output = []
        
        for i in splited_string: 
            output.append(i[1:][::-1]) 
        return " ".join(output)
