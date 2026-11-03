class Solution:

  def findContentChildren(self, g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()

    child_i = 0
    cookie_j = 0

    while child_i < len(g) and cookie_j < len(s):
      if s[cookie_j] >= g[child_i]:
        # Cookie satisfies the child, move to the next child
        child_i += 1
      # Always move to the next cookie
      cookie_j += 1

    return child_i