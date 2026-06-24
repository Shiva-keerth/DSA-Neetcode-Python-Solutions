class Solution:
    def maxDepth(self, root) -> int:
        """
        Time: O(n) | Space: O(h)
        Recursive DFS approach.
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
