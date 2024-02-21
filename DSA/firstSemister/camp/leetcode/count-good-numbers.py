class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return pow(20,n//2,10**9+7) if n%2 == 0 else (pow(20,n//2,10**9+7)*5)%(10**9+7) 