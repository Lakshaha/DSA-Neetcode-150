class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        high = len(nums1)
        if high % 2 != 0:
            return nums1[high//2 ]
        else:
            return (nums1[high//2 - 1] + nums1[high//2])/2
