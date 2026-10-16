class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.sum_val = [0] * (4 * n)
        self.MOD = 10**9 + 7

    def _push(self, node, l, r):
        if self.lazy[node] != 0:
            val = self.lazy[node]
            mid = (l + r) // 2
            
            # Apply to left child
            self._apply(2 * node, l, mid, val)
            # Apply to right child
            self._apply(2 * node + 1, mid + 1, r, val)
            
            self.lazy[node] = 0

    def _apply(self, node, l, r, val):
        # (cnt + val)^2 = cnt^2 + 2*val*cnt + val^2 * length
        length = (r - l + 1)
        self.tree[node] = (
            self.tree[node] 
            + 2 * val * self.sum_val[node] 
            + val * val * length
        ) % self.MOD
        
        self.sum_val[node] = (self.sum_val[node] + val * length) % self.MOD
        self.lazy[node] = (self.lazy[node] + val) % self.MOD

    def update(self, node, l, r, ql, qr, val):
        if ql > r or qr < l:
            return
        if ql <= l and r <= qr:
            self._apply(node, l, r, val)
            return
        
        self._push(node, l, r)
        mid = (l + r) // 2
        self.update(2 * node, l, mid, ql, qr, val)
        self.update(2 * node + 1, mid + 1, r, ql, qr, val)
        
        self.tree[node] = (self.tree[2 * node] + self.tree[2 * node + 1]) % self.MOD
        self.sum_val[node] = (self.sum_val[2 * node] + self.sum_val[2 * node + 1]) % self.MOD

    def query_sum(self):
        return self.tree[1]


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        seg = SegmentTree(n)
        
        last_occurrence = {}
        total_sum = 0
        current_sum_squares = 0
        
        for i, x in enumerate(nums):
            j = last_occurrence.get(x, -1)
            last_occurrence[x] = i
            
            # Update segment tree for range [j + 1, i] with increment +1
            seg.update(1, 0, n - 1, j + 1, i, 1)
            
            # Total sum of squares of all subarrays ending at index i
            total_sum = (total_sum + seg.query_sum()) % MOD
            
        return total_sum