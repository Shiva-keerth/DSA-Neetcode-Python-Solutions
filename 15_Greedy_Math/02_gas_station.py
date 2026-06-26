class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """
        Time: O(n) | Space: O(1)
        Greedy approach checking total and current diffs.
        """
        if sum(gas) < sum(cost):
            return -1
            
        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                res = i + 1
        return res
