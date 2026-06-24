class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Time: O(n) | Space: O(1)
        Bottom-up dynamic programming.
        """
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one
