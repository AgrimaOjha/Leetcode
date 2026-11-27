from typing import List


class Solution:

  def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
    max_f = max(f for f, _ in items)

    # Count how many items have each exact factor
    exact_cnt = [0] * (max_f + 1)
    for f, _ in items:
      exact_cnt[f] += 1

    # For each factor f, count how many items have factor divisible by f
    div_cnt = [0] * (max_f + 1)
    for f in range(1, max_f + 1):
      for mult in range(f, max_f + 1, f):
        div_cnt[f] += exact_cnt[mult]

    # dp[b] = max total item copies (purchased + free) with budget b
    dp = [0] * (budget + 1)

    for f, price in items:
      if price > budget:
        continue

      # Free copies granted by buying at least 1 copy of this item (j != i)
      free_gain = div_cnt[f] - 1

      # 1) First copy of this item: +1 purchased copy + free_gain free copies (0/1 style)
      first_gain = 1 + free_gain
      for b in range(budget, price - 1, -1):
        if dp[b - price] + first_gain > dp[b]:
          dp[b] = dp[b - price] + first_gain

      # 2) Subsequent copies of this item: +1 copy per purchase (unbounded style)
      for b in range(price, budget + 1):
        if dp[b - price] + 1 > dp[b]:
          dp[b] = dp[b - price] + 1

    return max(dp)