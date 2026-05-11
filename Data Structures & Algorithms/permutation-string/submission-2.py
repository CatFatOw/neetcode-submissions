from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        mapping_s1 = defaultdict(int)
        mapping_s2 = defaultdict(int)

        for char in s1:
            mapping_s1[char] += 1
        k = len(s1)
        left = 0

        for i in range(k):
            mapping_s2[s2[i]] += 1
        if mapping_s2 == mapping_s1:
            return True 

        for i in range(k, len(s2)):
            mapping_s2[s2[i]] += 1
            mapping_s2[s2[i-k]] -= 1
            if mapping_s2[s2[i-k]] <= 0:
                mapping_s2.pop(s2[i-k])
            if mapping_s2 == mapping_s1:
                return True 
        return False




