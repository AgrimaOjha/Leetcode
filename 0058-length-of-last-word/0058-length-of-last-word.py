class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip trailing spaces, split the string into words, and return the length of the last word
        return len(s.strip().split()[-1])