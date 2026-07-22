class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged: List[int] = list()
        i: int = 0
        j: int = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        n: int = len(merged)
        middle: int = n // 2
        if n % 2 == 1:
            return merged[middle]
        return (merged[middle - 1] + merged[middle]) / 2