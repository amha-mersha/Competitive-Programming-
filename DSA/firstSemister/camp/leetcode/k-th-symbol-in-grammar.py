class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        path = []
        for i in range(n):
            path.append(k)
            k = math.ceil(k/2)
        path.sort()
        def backtrack(bit,row,col,ptr):
            if row == n:
                return bit
            nxt = col*2
            if bit == 0:
                return backtrack(0,row+1,nxt-1,ptr+1) if nxt-1 == path[ptr] else backtrack(1,row+1,nxt,ptr+1)  
            else:
                return backtrack(1,row+1,nxt-1,ptr+1) if nxt-1 == path[ptr] else backtrack(0,row+1,nxt,ptr+1)  
        return backtrack(0,0,1,0)