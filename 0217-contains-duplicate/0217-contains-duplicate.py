from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans=set(nums)
        return len(nums)!=len(ans)