from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        mapping = defaultdict(int)

        for char in s:
            mapping[char] += 1
        
        evens = 0
        odds = 0
        found = False
        for val, freq in mapping.items():
            if freq % 2 == 0:
                evens +=  freq
            else:
                odds += freq-1
                found = True
        
        total = 0
        if found:
            total += 1
        
        total += evens + odds
        return total