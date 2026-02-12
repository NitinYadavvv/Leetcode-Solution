# Last updated: 2/12/2026, 10:51:14 PM
from collections import deque
class RideSharingSystem:

    def __init__(self):
        self.rider = deque()
        self.driver = deque()

    def addRider(self, riderId: int) -> None:
        self.rider.append(riderId)
       
    def addDriver(self, driverId: int) -> None:
        self.driver.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if len(self.rider) == 0 or len(self.driver) == 0:
            return[-1,-1]
        return [self.driver.popleft(),self.rider.popleft()]


    def cancelRider(self, riderId: int) -> None:
        if riderId in self.rider:
            self.rider.remove(riderId)

# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)