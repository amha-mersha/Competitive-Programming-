class Solution:
    def __init__(self):
        self.stack  = []
        self.result = []
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(opn, close):
            if opn == close == n:
                curr = self.stack.copy()
                self.result.append("".join(curr))
                return 
            if opn < n:
                self.stack.append('(')
                backtrack(opn + 1, close)
                self.stack.pop()
            if close < opn:
                self.stack.append(")")
                backtrack(opn, close + 1)
                self.stack.pop()
            return 
        backtrack(0,0)
        return self.result