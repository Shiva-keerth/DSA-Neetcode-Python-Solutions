class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        Time: O(n) | Space: O(1)
        Greedy backwards approach.
        """
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
