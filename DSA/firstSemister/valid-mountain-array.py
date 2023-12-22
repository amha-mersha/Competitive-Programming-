class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        growth = True
        for i in range(len(arr) - 1):
            if growth:
                if arr[i] > arr[i + 1]:
                    if i == 0:
                        return False
                    growth = False
                elif arr[i] == arr[i + 1]:
                    return False
            elif arr[i] <= arr[i + 1]:
                return False
        return not growth