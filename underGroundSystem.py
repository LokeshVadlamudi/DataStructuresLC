class UnderGround:
    def __init__(self):
        self.passenger = {}
        self.avgTime = {}
        pass

    def checkin(self, pid: int, stationName: str, t: int):
        self.passenger[pid] = (stationName,t)
        pass

    def checkout(self, pid: int, stationName: str, t: int):
        if pid in self.passenger.keys():
            if self.passenger[pid][0]+stationName not in self.avgTime:
                self.avgTime[self.passenger[pid][0]+stationName] = t - self.passenger[pid][1]
            else:
                self.avgTime[self.passenger[pid][0] + stationName] = (self.avgTime[self.passenger[pid][0]+stationName] + (t - self.passenger[pid][1] + t)) / 2
        del self.passenger[pid]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        print(self.avgTime)
        print(self.passenger)
        return self.avgTime[startStation+endStation]
        pass


a = UnderGround()
a.checkin(45, "Leyton", 3)
a.checkin(32, "Paradise", 8)
a.checkin(27, "Leyton", 10)
a.checkout(45, "Waterloo", 15)
a.checkout(27, "Waterloo", 20)
a.checkout(32, "Cambridge", 22)
print(a.getAverageTime("Paradise", "Cambridge"))





