from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_map = defaultdict(list)
        
        for s in strs:
            # Sort the characters to create a unique key for all anagrams
            sorted_key = "".join(sorted(s))
            anagrams_map[sorted_key].append(s)
            
        return list(anagrams_map.values())