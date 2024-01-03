class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        count = 0
        l,r = 0,len(people)-1
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            count += 1
            r -= 1
        return count
        