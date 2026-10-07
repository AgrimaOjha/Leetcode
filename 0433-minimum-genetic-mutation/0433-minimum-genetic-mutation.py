from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        queue = deque([(startGene, 0)])
        visited = {startGene}
        
        while queue:
            gene, steps = queue.popleft()
            
            if gene == endGene:
                return steps
            
            # Try changing each character to 'A', 'C', 'G', 'T'
            for i in range(len(gene)):
                for char in "ACGT":
                    if char != gene[i]:
                        mutated = gene[:i] + char + gene[i+1:]
                        if mutated in bank_set and mutated not in visited:
                            visited.add(mutated)
                            queue.append((mutated, steps + 1))
                            
        return -1