class Solution:
    def bestClosingTime(self, customers: str) -> int:
        early_hour = 0
        penality = 0
        curr = 0
        for i in range(len(customers)):
            if customers[i] == "Y":
                curr -= 1
                if curr < penality:
                    penality = curr
                    early_hour = i + 1
            else:
                curr += 1
        return early_hour