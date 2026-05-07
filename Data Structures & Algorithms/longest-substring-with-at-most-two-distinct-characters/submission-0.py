from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        distinct_char = defaultdict(int)
        left = 0
        ans = 0

        for right in range(len(s)):
            distinct_char[s[right]] += 1
        
            while len(distinct_char) > 2:
                distinct_char[s[left]] -= 1
                if distinct_char[s[left]] <= 0:
                    distinct_char.pop(s[left])
                    
                left += 1
            ans = max(ans, right - left + 1)
        return ans

        