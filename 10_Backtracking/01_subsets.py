class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        Time: O(n * 2^n) | Space: O(n)
        Backtracking to explore include/exclude decisions.
        """
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
                
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
            
        dfs(0)
        return res
