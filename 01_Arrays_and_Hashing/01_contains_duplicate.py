class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Time: O(n) | Space: O(n)
        Uses a hashset to keep track of seen numbers.
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
