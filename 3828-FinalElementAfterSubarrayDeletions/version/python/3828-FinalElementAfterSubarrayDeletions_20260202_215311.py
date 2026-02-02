# Last updated: 2/2/2026, 9:53:11 PM
1from collections import deque
2class RideSharingSystem:
3
4    def __init__(self):
5        self.rider = deque()
6        self.driver = deque()
7
8    def addRider(self, riderId: int) -> None:
9        self.rider.append(riderId)
10       
11    def addDriver(self, driverId: int) -> None:
12        self.driver.append(driverId)
13
14    def matchDriverWithRider(self) -> List[int]:
15        if len(self.rider) == 0 or len(self.driver) == 0:
16            return[-1,-1]
17        return [self.driver.popleft(),self.rider.popleft()]
18
19
20    def cancelRider(self, riderId: int) -> None:
21        if riderId in self.rider:
22            self.rider.remove(riderId)
23
24# Your RideSharingSystem object will be instantiated and called as such:
25# obj = RideSharingSystem()
26# obj.addRider(riderId)
27# obj.addDriver(driverId)
28# param_3 = obj.matchDriverWithRider()
29# obj.cancelRider(riderId)