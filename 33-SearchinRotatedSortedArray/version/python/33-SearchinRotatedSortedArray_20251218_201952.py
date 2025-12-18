# Last updated: 12/18/2025, 8:19:52 PM
# first ill find the pivot from where array is defltect then first search in 0 to pivot after if not found then pivot+1 to end
1class Solution(object):
2    def search(self, arr, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        def pivot(arr):
9            low = 0
10            high = len(arr)-1
11            while low<=high:
12                mid = (low + high)//2
13                if mid<high and arr[mid]>arr[mid+1]:
14                    return mid
15                if mid>low and arr[mid]<arr[mid-1]:
16                    return mid-1
17                if arr[low] > arr[mid]:
18                    high = mid-1
19                else:
20                    low = mid+1
21            return -1
22
23        def binary(arr,low,high,target):
24
25            if low>high:
26                return -1
27
28            mid = (low+high)//2
29
30            if arr[mid]==target:
31                return mid
32            elif arr[mid]>target:
33                return binary(arr,low,mid-1,target)
34            else:
35                return binary(arr,mid+1,high,target)
36
37        pi = pivot(arr)
38
39        if pi == -1:
40            return binary(arr, 0, len(arr) - 1, target)
41
42        if arr[pi] == target:
43            return pi
44        left = binary(arr, 0, pi - 1, target)
45        if left != -1:
46            return left
47
48        return binary(arr, pi + 1, len(arr) - 1, target)
49
50        
51        
52
53            
54            
55                    
56
57
58        