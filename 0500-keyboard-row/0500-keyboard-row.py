class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        # Define the three keyboard rows as sets of characters
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        
        for word in words:
            # Convert to lowercase to handle case-insensitivity
            word_set = set(word.lower())
            
            # Check if all characters of the word belong to any single row
            if word_set.issubset(row1) or word_set.issubset(row2) or word_set.issubset(row3):
                result.append(word)
                
        return result