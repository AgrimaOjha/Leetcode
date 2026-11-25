from collections import Counter
from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        # Two independent polynomial rolling hashes to minimize collision risk
        base1, mod1 = 1_000_003, (1 << 61) - 1
        base2, mod2 = 1_000_033, 1_000_000_007

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)

        for i, val in enumerate(nums):
            # Shift values by +1 so 0 doesn't collapse under multiplication
            x = val + 1
            pow1[i + 1] = (pow1[i] * base1) % mod1
            pow2[i + 1] = (pow2[i] * base2) % mod2
            pref1[i + 1] = (pref1[i] * base1 + x) % mod1
            pref2[i + 1] = (pref2[i] * base2 + x) % mod2

        def get_hash(l: int, r: int) -> tuple[int, int]:
            # Hash of nums[l:r] (half-open interval of length r - l)
            length = r - l
            h1 = (pref1[r] - pref1[l] * pow1[length]) % mod1
            h2 = (pref2[r] - pref2[l] * pow2[length]) % mod2
            return (h1, h2)

        def has_unique_of_length(length: int) -> bool:
            counts = Counter()
            for start in range(n - length + 1):
                counts[get_hash(start, start + length)] += 1
            return any(freq == 1 for freq in counts.values())

        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique_of_length(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans