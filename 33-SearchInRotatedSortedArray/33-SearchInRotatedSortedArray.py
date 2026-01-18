# Last updated: 1/18/2026, 6:22:05 PM
class Solution(object):
    def search(self, arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def pivot(arr):
            low = 0
            high = len(arr)-1
            while low<=high:
                mid = (low + high)//2
                if mid<high and arr[mid]>arr[mid+1]:
                    return mid
                if mid>low and arr[mid]<arr[mid-1]:
                    return mid-1
                if arr[low] > arr[mid]:
                    high = mid-1
                else:
                    low = mid+1
            return -1

        def binary(arr,low,high,target):

            if low>high:
                return -1

            mid = (low+high)//2

            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                return binary(arr,low,mid-1,target)
            else:
                return binary(arr,mid+1,high,target)

        pi = pivot(arr)

        if pi == -1:
            return binary(arr, 0, len(arr) - 1, target)

        if arr[pi] == target:
            return pi
        left = binary(arr, 0, pi - 1, target)
        if left != -1:
            return left

        return binary(arr, pi + 1, len(arr) - 1, target)

        
        

            
            
                    


        