from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping1 = defaultdict(int)
        mapping2 = defaultdict(int)

        for char in s:
            mapping1[char] += 1
        for char in t:
            mapping2[char] += 1
        return mapping1 == mapping2

        