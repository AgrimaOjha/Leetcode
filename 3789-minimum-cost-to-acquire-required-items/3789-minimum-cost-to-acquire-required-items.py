class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # If buying two separate items (one for type 1 and one for type 2) 
        # is cheaper than a 'both' item, cap costBoth at their sum.
        costBoth = min(costBoth, cost1 + cost2)
        
        # Use min(need1, need2) pairs of type 3 items if costBoth is cheaper
        common_count = min(need1, need2)
        total_cost = common_count * min(costBoth, cost1 + cost2) # or min(costBoth, ...)
        
        # Actually, let's look at the optimal greedy strategy:
        # 1. We need min(need1, need2) units of both requirements. We can get them either using 
        #    a 'both' item or 1 of type 1 + 1 of type 2.
        cost_common = min(costBoth, cost1 + cost2)
        
        # 2. For the remaining requirements:
        rem1 = need1 - common_count
        rem2 = need2 - common_count
        
        total_cost = common_count * cost_common
        
        # For remaining type 1, we can use type 1 or type 3
        total_cost += rem1 * min(cost1, costBoth)
        
        # For remaining type 2, we can use type 2 or type 3
        total_cost += rem2 * min(cost2, costBoth)
        
        return total_cost