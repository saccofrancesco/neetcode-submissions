class Solution:
    def trap(self, height: List[int]) -> int:
        left: int = 0
        right: int = len(height) - 1
        left_max: int = 0
        right_max: int = 0
        trapped_water: int = 0
        while left < right:
            if height[left] <= height[right]:
                left_max: int = max(left_max, height[left])
                trapped_water += left_max - height[left]
                left += 1
            else:
                right_max: int = max(right_max, height[right])
                trapped_water += right_max - height[right]
                right -= 1
        return trapped_water
