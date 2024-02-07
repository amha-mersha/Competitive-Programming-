class Solution:
    def shiftingLetters(self, s, shifts):
        prefix = [0]*(len(s) + 1)
        for start,ended,direction in shifts:
            if direction:
                prefix[start] += 1
                prefix[ended + 1] -= 1
            else:
                prefix[start] -= 1
                prefix[ended + 1] += 1
        
        current = 0
        for i in range(len(s)):
            current += prefix[i]
            newItem = (((ord(s[i]) + current-97)%26)+97)
            s = s[:i] + chr(newItem) + s[i+1:]
        return s