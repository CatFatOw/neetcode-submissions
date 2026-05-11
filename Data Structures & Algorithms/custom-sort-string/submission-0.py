from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        all characters of order are unique and sorted in some custom order previously

        premute s so that it matches the order of order 

        Apporach: 
        create a mapping of s
        based on the order, we just create ht out * freq
        """
        mapping = defaultdict(int)
        for char in s:
            mapping[char] += 1
        
        out = ""
        used = set()
        for char in order:
            if char in mapping:
                out += char * mapping[char]
                used.add(char)
            
        for char in s:
            if char not in used:
                out += char
        
        return out

        