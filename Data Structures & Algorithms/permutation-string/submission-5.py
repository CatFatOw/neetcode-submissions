from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Essentially check if frequecy map of fixed sliding window of len(s1) exists in s2. 

        Use sliding window
        """
        if len(s1) > len(s2):
            return False 
        
        s1_mapping = defaultdict(int)
        window_mapping = defaultdict(int)

        # populate 1_mapping
        for char in s1:
            s1_mapping[char] += 1
        # Fixed sliding window approach
        for i in range(len(s1)):
            window_mapping[s2[i]] += 1

        if window_mapping == s1_mapping:
            return True 
        
        k = len(s1)
        for i in range(k, len(s2)):
            window_mapping[s2[i-k]] -=1
            if window_mapping[s2[i-k]] <= 0:
                window_mapping.pop(s2[i-k])
            window_mapping[s2[i]] += 1
            if window_mapping == s1_mapping:
                return True 
        return False

        