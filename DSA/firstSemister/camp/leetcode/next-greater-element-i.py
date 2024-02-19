class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        track = defaultdict(lambda:-1)
        stack = []
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                track[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        res = []
        for i in nums1:
            res.append(track[i])
        return res