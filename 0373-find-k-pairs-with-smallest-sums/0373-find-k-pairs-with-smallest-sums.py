import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        if not nums1 or not nums2 or k <= 0:
            return []
        
        min_heap = []
        result = []
        
        # Initialize the heap with pairs from nums1 and the first element of nums2
        for i in range(min(k, len(nums1))):
            # Store (sum, nums1_val, nums2_index)
            heapq.heappush(min_heap, (nums1[i] + nums2[0], nums1[i], 0, i))
            
        # Extract up to k smallest pairs
        while min_heap and len(result) < k:
            current_sum, u, j, i = heapq.heappop(min_heap)
            result.append([u, nums2[j]])
            
            # If there is a next element in nums2, push it into the heap
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], nums1[i], j + 1, i))
                
        return result