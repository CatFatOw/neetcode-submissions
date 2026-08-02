from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        mapping = defaultdict(int)
        longest = 0
        left = 0

        for right in range(len(s)):
            mapping[s[right]] += 1
        
            while len(mapping) > 2:
                mapping[s[left]] -= 1
                if mapping[s[left]] <= 0:
                    mapping.pop(s[left])
                left += 1
            longest = max(longest, right-left+1)
        return longest
        