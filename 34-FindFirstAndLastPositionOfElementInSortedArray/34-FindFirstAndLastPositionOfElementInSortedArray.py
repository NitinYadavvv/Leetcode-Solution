# Last updated: 12/10/2025, 8:24:41 AM
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums)-1
        l=[]
        while(i<=j):
            mid = i+(j-i)//2
            if nums[mid] == target:
               if mid == 0 or nums[mid]> nums[mid-1]:
                    l.append(mid)
                    break
               else:
                    j=mid-1
            elif nums[mid] > target:
                j = mid-1
            else:
                i = mid+1
        if i>j:
            l.append(-1)
        i = 0
        j = len(nums)-1
        while(i<=j):
            mid = i+(j-i)//2
            if nums[mid] == target:
               if mid== len(nums)-1 or nums[mid]< nums[mid+1]:
                    l.append(mid)
                    break
               else:
                    i=mid+1
            elif nums[mid] > target:
                j = mid-1
            else:
                i = mid+1
        if i>j:
            l.append(-1)
        return l
        
        
                

                    
                    


        