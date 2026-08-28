class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            char = s[right]
            
            # If the character is already in the map and within the current window
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            # Store/update the latest index of the character
            char_map[char] = right
            
            # Update the maximum length found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length