class Solution:
    def decodeString(self, s: str,idx = 0) -> str:
        def helper(idx):
            nonlocal s
            dgt = 0
            string = ""
            while idx < len(s):
                if s[idx] == "[":
                    idx, strg = helper(idx + 1)
                    string += strg*dgt
                    dgt = 0
                elif s[idx] == "]":
                    return idx , string
                elif s[idx].isdigit():
                    dgt = dgt * 10 + int(s[idx])
                else:
                    string += s[idx]
                idx += 1
            return idx, string
        _,res = helper(0)
        return res