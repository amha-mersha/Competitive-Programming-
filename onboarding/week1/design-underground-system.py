class UndergroundSystem(object):

    def __init__(self):
        self.temp = {}
        self.averageTimes = {}
    def checkIn(self, id, stationName, t):
        self.temp[id] = [stationName,t]
        
    def checkOut(self, id, stationName, t):
        curr = t - self.temp[id][1]
        name = (self.temp[id][0],stationName)
        if name in self.averageTimes:
            self.averageTimes[name].append(curr)
        else:
            self.averageTimes[name] = [curr]

    def getAverageTime(self, startStation, endStation):
        return sum(self.averageTimes[(startStation,endStation)])/len(self.averageTimes[(startStation,endStation)])