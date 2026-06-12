class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(n) | Space: O(1) assuming lowercase english letters
        Counts character frequencies.
        """
        if len(s) != len(t): return False
        
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
            
        return all(c == 0 for c in count)
