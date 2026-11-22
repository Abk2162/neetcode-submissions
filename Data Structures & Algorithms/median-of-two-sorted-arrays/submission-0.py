class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = nums1 + nums2
        new.sort()
        if len(new) % 2 == 0:
            mid = len(new) // 2
            return ((new[mid] + new[mid-1]) / 2)
        else:
            mid = len(new) // 2
            return new[mid]