from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapping = defaultdict(int)
        left = 0
        ans = 0

        for right in range(len(s)):
            mapping[s[right]] += 1

            while mapping[s[right]] > 1:
                mapping[s[left]] -= 1
                if mapping[s[left]] <= 0:
                    mapping.pop(s[left])
                left += 1
            ans = max(ans, right - left + 1)
        return ans
        