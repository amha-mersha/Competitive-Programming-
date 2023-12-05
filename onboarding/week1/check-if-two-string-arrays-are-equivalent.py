class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        one = ""
        for i in word1:
            one += i
        two = ""
        for i in word2:
            two += i
        return one == two
        