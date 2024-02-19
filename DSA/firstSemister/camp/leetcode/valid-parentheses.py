class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "{([":
                stack.append(i)
            elif i == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif i == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
        return False if stack else True

