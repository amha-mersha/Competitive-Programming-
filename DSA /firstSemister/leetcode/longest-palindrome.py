class Solution:
    def longestPalindrome(self, s: str) -> int:
        track = Counter(s)
        remainder = False
        count = 0
        for i in track:
            if track[i]%2:
                remainder = True
                count += track[i] - 1
            else:
                count += track[i]
        if remainder:
            count += 1
        return count
