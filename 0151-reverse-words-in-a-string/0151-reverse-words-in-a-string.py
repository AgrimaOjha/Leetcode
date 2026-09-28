class Solution:
    def reverseWords(self, s: str) -> str:
        # split() handles extra spaces, [::-1] reverses the list, join() connects with a single space
        return " ".join(s.split()[::-1])