import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Initialize a min-heap with the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        # Iterate through the remaining elements
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
                
        # The root of the min-heap is the kth largest element
        return min_heap[0]