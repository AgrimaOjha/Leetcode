class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1      # Pointer for last valid element in nums1
        p2 = n - 1      # Pointer for last element in nums2
        p = m + n - 1   # Pointer for last position in nums1

        # Compare elements from the back and place the larger one at position p
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, copy them over
        # (Remaining elements in nums1 are already in their correct position)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1