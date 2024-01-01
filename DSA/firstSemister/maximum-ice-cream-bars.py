class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        bucket = [0 for i in range(max(costs))]
        for i in costs:
            bucket[i-1] += 1
        count = 0
        for i in range(len(bucket)):
            if coins - bucket[i]*(i+1) >= 0:
                coins -= bucket[i]*(i+1)
                count += bucket[i]
            else:
                while coins > 0 and bucket[i] > 0:
                    coins -= (i+1)
                    if coins >= 0:
                        count += 1
                    bucket[i] -= 1
            if coins <= 0:
                break

        return count