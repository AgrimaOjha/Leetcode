class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        next_greater = {}
        
        # Find the next greater element for each number in nums2 using a monotonic stack
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
            
        # Any remaining elements in the stack have no next greater element
        while stack:
            next_greater[stack.pop()] = -1
            
        # Construct the result for nums1 using our hash map
        return [next_greater[num] for num in nums1]