class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        total = [0 for i in range(n)]
        for l,r,val in bookings:
            total[l-1] += val
            if r < n:
                total[r] -= val
        for i in range(1,n):
            total[i] += total[i-1]
        return total