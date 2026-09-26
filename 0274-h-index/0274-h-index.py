class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        counts = [0] * (n + 1)
        
        # Count frequencies of each citation value up to n
        for c in citations:
            if c >= n:
                counts[n] += 1
            else:
                counts[c] += 1
        
        # Accumulate paper counts from highest citations to lowest
        total_papers = 0
        for h in range(n, -1, -1):
            total_papers += counts[h]
            if total_papers >= h:
                return h
                
        return 0