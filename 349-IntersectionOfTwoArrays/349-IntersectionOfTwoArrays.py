# Last updated: 12/10/2025, 8:21:53 AM
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        h = {}
        i = 0
        j = 0
        nums1.sort()
        nums2.sort()
        while i<len(nums1) and j<len(nums2):
            if nums1[i]>nums2[j]:
                j+=1
            elif nums1[i]==nums2[j]:
                h[nums1[i]] = 1
                i+=1
                j+=1
            else:
                i+=1
        return list(h)

        