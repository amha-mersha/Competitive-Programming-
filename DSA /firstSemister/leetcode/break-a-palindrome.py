class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)
        lgth = len(palindrome) 
        if lgth == 1:
            return ""
        odd = lgth%2 == 1
        if odd:
            for idx,itm in enumerate(palindrome):
                if idx != lgth//2  and itm != "a":
                    palindrome[idx] = "a"
                    return "".join(palindrome)
        else:
            for idx,itm in enumerate(palindrome):
                if itm != "a":
                    palindrome[idx] = "a"
                    return "".join(palindrome)
        palindrome[-1] = "b"
        return "".join(palindrome)