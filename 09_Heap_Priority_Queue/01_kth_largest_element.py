import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Time: O(n log k) | Space: O(k)
        Using a min-heap of size k.
        """
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
                
        return min_heap[0]
