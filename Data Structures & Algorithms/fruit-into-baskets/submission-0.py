
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mapping = defaultdict(int)
        left = 0
        max_length = 0
        
        for right in range(len(fruits)):
            mapping[fruits[right]] += 1
            
            while len(mapping) > 2:
                mapping[fruits[left]] -= 1
                if mapping[fruits[left]] <= 0:
                    mapping.pop(fruits[left])
                left += 1
            max_length = max(max_length, right-left+1)
        return max_length
                
        
