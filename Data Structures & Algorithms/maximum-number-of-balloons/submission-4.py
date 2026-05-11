from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        valid_frequency = {"b":1, "a":1, "l":2, "o":2, "n":1} 
        mapping = defaultdict(int)

        for char in text:
            if char in valid_frequency:
                mapping[char] += 1
        
        if len(mapping) != len(valid_frequency):
            return 0
        chars = []
        for char, freq in mapping.items():

            if freq < valid_frequency[char]:
                return 0
            if char != "l" and char != "o":
                chars.append(freq)
            else:
                chars.append(freq//2)
        
       
        return min(chars)
    