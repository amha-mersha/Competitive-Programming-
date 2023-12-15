class FrequencyTracker:

    def __init__(self):
        self.freq = defaultdict(int)
        self.freq_freq = defaultdict(int)

    def add(self, number: int) -> None:
        self.freq[number] += 1
        self.freq_freq[self.freq[number]] += 1
        if self.freq_freq[self.freq[number]-1]:
            self.freq_freq[self.freq[number]-1] -= 1

    def deleteOne(self, number: int) -> None:
        if self.freq[number]:   
            self.freq[number] -= 1
            self.freq_freq[self.freq[number]] += 1
            if self.freq_freq[self.freq[number]+1]:  
                self.freq_freq[self.freq[number]+1] -= 1

    def hasFrequency(self, frequency: int) -> bool:
        if self.freq_freq[frequency] > 0:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)