from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapping = defaultdict(int)
        longest = 0
        left = 0
        max_freq = 0
        
        for right in range(len(s)):
            mapping[s[right]] += 1
            max_freq = max(mapping.values())
            replacement = (right-left+1)-max_freq
            
            while replacement > k:
                mapping[s[left]] -= 1
                if mapping[s[left]] <= 0:
                    mapping.pop(s[left])
                left += 1
                    
                max_freq = max(mapping.values())
                replacement = (right-left+1)-max_freq
            longest = max(longest, right-left+1)
        return longest

       