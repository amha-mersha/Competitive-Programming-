class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        kye = {}
        for i in range(len(arr2)):
            kye[arr2[i]] = i
        def sorter(x):
            if x in kye:
                return kye[x]
            return len(arr2)+x
        arr1.sort( key = sorter)
        return arr1