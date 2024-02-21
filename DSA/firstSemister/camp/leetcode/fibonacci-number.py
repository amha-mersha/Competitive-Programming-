class Solution(object):
    def fib(self, n):
        catch = {}
        def recurr_fib(n):
            if n in catch:
                return catch[n]
            if n < 2:
                result = n
            else:
                result = recurr_fib(n-1) + recurr_fib(n-2)
            catch[n] = result
            return result 
        return recurr_fib(n)