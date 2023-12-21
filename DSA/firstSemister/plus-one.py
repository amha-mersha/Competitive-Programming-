class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry = 1
        for i in range(len(digits)):
            curr = digits[i] + carry
            digits[i] = curr%10
            carry = curr//10
        if carry:
            digits.append(carry)
        return digits[::-1]
            