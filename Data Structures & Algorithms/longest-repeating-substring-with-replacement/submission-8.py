
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 1
        targets = set()
        for char in s:
            targets.add(char)
        
        for target in targets:
            counter = 0
            left = 0
            for right in range(len(s)):
                if s[right] != target:
                    counter += 1
                
                while counter > k and left < right:
                    if s[left] != target:
                        counter -= 1
                    left += 1
                longest = max(longest, right-left+1)
        return longest

        