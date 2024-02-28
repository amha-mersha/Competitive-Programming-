class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5
        def helper(n):
            if n == 2:
                return 20
            if n%4 == 0:
                curr = (helper(n//2))%(10**9 + 7)
                return (curr*curr)%(10**9 + 7)
            if n%2 == 1:
                return (5* helper(n-1))%(10**9 + 7)
            return (4* helper(n-1))%(10**9 + 7)
        return helper(n)