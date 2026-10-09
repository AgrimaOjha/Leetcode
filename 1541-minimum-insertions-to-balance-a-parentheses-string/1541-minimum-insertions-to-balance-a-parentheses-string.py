class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        right_needed = 0
        
        for char in s:
            if char == '(':
                # Each '(' needs 2 ')'
                right_needed += 2
                
                # If right_needed is odd, it means we had an unmatched single ')' 
                # that was expecting a second ')' before this new '('
                if right_needed % 2 == 1:
                    insertions += 1    # Insert a ')' to complete the previous pair
                    right_needed -= 1  # Reduce the needed count accordingly
            else:
                # We found a ')'
                right_needed -= 1
                
                # If right_needed becomes -1, we encountered a ')' without a preceding '('
                if right_needed == -1:
                    insertions += 1    # Insert a '('
                    right_needed += 2  # The inserted '(' expects 2 ')', one of which is the current ')'
                    
        return insertions + right_needed