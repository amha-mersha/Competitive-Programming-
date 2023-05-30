class Solution():
    def select(self, arr, i):
        low = i
        for idx in range(i+1, len(arr)):
            if arr[low] > arr[idx]:
                low = idx
        
        return low
            
    
    def selectionSort(self, arr,n):
        for i in range(n):
            j = self.select(arr,i)
            arr[i], arr[j] = arr[j], arr[i]
            
        return arr
