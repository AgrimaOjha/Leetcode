class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Convert both lists to sets and find their intersection, then convert back to a list
        return list(set(nums1) & set(nums2))