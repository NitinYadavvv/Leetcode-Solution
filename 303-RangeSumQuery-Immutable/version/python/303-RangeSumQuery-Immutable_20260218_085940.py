# Last updated: 2/18/2026, 8:59:40 AM
1class NumArray:
2
3    def __init__(self, nums: List[int]):
4        self.org = nums
5        for i in range(1,len(nums)):
6            nums[i] += nums[i-1]
7
8        self.arr = nums
9
10    def sumRange(self, left: int, right: int) -> int:
11        if left == 0:
12            return self.arr[right]
13
14        return self.arr[right]-self.arr[left-1]
15        
16
17
18# Your NumArray object will be instantiated and called as such:
19# obj = NumArray(nums)
20# param_1 = obj.sumRange(left,right)