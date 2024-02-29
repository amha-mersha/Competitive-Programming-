class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = [""]
        numpad = ['abc','def', 'ghi', 'jkl', 'mno', 'pqrs','tuv', 'wxyz']
        for i in digits:
            temp = []
            for j in numpad[int(i)-2]:
                for k in result:
                    temp.append(k+j)
            result = temp
        return result