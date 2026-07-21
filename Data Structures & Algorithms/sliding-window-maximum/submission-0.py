class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left: int = 0
        right: int = k - 1
        maximums: List[int] = list()
        while right < len(nums):
            maximums.append(max(nums[left:right + 1]))
            left += 1
            right += 1
        return maximums