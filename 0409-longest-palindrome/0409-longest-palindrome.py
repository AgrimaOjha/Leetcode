from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        has_odd = False
        
        for count in counts.values():
            # Add the largest even part of the frequency
            length += (count // 2) * 2
            
            # If the frequency is odd, we can use one odd character in the center
            if count % 2 == 1:
                has_odd = True
                
        # If there's at least one character with an odd count, 
        # we can place one in the middle of the palindrome
        if has_odd:
            length += 1
            
        return length