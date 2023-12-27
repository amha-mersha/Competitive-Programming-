class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        one = defaultdict(int)
        two = defaultdict(int)
        for i in nums1:
            one[i] += 1
        for i in nums2:
            two[i] += 1
        res = []
        for i in one:
            for j in range(min(one[i],two[i])):
                res.append(i)
        return res