class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Time: O(log n) | Space: O(1)
        Standard binary search.
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
