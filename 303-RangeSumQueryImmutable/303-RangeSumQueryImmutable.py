# Last updated: 2/26/2026, 7:48:26 AM
class NumArray:

    def __init__(self, nums: List[int]):
        self.org = nums
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        self.arr = nums

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.arr[right]

        return self.arr[right]-self.arr[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)