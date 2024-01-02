class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()
        res = 0
        for i in range(0,len(processorTime)):
            res = max(res,tasks[i*4] + processorTime[i] )
        return res


        