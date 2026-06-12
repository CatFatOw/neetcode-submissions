from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        map_s1 = defaultdict(int)
        map_s2 = defaultdict(int)

        # Populate this
        for char in s1:
            map_s1[char] += 1

        # Logic: Use a fixed sliding window
        for i in range(len(s1)):
            char = s2[i]
            map_s2[char] += 1
        if map_s1 == map_s2:
            return True 

        for i in range(len(s1), len(s2)):
            char = s2[i]
            map_s2[char] += 1
            # remove previous
            map_s2[s2[i-len(s1)]] -= 1
            if map_s2[s2[i-len(s1)]] <= 0:
                map_s2.pop(s2[i-len(s1)])

            if map_s2 == map_s1:
                return True 
        return False
        
                