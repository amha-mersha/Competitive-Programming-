class Solution(object):
    def average(self, salary):
        total = sum(salary)
        total -= (max(salary) + min(salary))
        return total/(float(len(salary)-2))
        