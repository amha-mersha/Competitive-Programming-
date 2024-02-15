class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = defaultdict(int)
        for idx, itm in enumerate(bills):
            change = itm-5
            if change == 15:
                if register[10] > 0 and register[5] > 0:
                    register[10] -= 1
                    register[5] -= 1
                elif register[5] > 2:
                    register[5] -= 3
                else:
                    return False
            elif change == 5:
                if register[5] > 0:
                    register[5] -= 1
                    register[10] += 1
                else:
                    return False
            else:
                register[5] += 1
        return True