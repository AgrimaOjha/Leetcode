class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        n = len(nums)
        # Pair each number with its original index
        indexed_nums = [(nums[i], i) for i in range(n)]

        # Sort based on digit sum, and then by value as tie-breaker
        indexed_nums.sort(key=lambda x: (get_digit_sum(x[0]), x[0]))

        # Map each number to its correct target index
        target_pos = {}
        for sorted_idx, (val, orig_idx) in enumerate(indexed_nums):
            target_pos[orig_idx] = sorted_idx

        # Find the number of cycles using visited array
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or target_pos[i] == i:
                continue
            
            # Traverse the cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = target_pos[curr]
                cycle_size += 1
            
            if cycle_size > 1:
                swaps += (cycle_size - 1)

        C = swaps
        return C