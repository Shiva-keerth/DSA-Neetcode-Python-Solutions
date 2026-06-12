class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Time: O(n) | Space: O(n)
        One-pass hash map solution.
        """
        prevMap = {} # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []
