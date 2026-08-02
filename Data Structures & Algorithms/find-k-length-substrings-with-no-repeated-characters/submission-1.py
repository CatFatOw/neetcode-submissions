from collections import defaultdict
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        mapping = defaultdict(int)
        total = 0
        for i in range(k):
            mapping[s[i]] += 1
        
        if len(mapping) == k:
            total += 1
        
        for i in range(k, len(s)):
            mapping[s[i-k]] -= 1
            
            if mapping[s[i-k]] <=0:
                mapping.pop(s[i-k])
            mapping[s[i]] += 1
            if len(mapping) == k:
                total += 1
            
        return total
        
       