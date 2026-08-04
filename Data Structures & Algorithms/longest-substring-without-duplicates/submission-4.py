from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        curr = 0
        left = 0

        mapping = defaultdict(int)

        for right in range(len(s)):
            mapping[s[right]] += 1
        
            while mapping[s[right]] >= 2:
                mapping[s[left]] -= 1
                left += 1
            longest = max(longest, right-left + 1)
        return longest



        