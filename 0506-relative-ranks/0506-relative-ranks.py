class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        n = len(score)
        # Pair each score with its original index
        sorted_scores = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        
        answer = [""] * n
        
        for rank, (original_index, s) in enumerate(sorted_scores):
            if rank == 0:
                answer[original_index] = "Gold Medal"
            elif rank == 1:
                answer[original_index] = "Silver Medal"
            elif rank == 2:
                answer[original_index] = "Bronze Medal"
            else:
                answer[original_index] = str(rank + 1)
                
        return answer