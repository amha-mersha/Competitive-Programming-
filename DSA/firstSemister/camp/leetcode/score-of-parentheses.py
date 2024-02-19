class Solution(object):
    def scoreOfParentheses(self, s):
        count = 0
        stack = []
        for item in s:
            if item == "(":
                stack.append(count)
                count = 0
            else:
                count = stack.pop() + max(2*count,1)
        return count