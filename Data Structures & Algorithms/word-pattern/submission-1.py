from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        pattern means there is a bijection between a letter in pattern and a word in s
        """
        p_s = defaultdict(int)
        s_p = defaultdict(int)
        p = pattern

        s = s.split()
        if len(pattern) != len(s):
            return False 
        
        for i in range(len(pattern)):
            if p[i] not in p_s:
                p_s[p[i]] = s[i]
            else:
                if s[i] != p_s[p[i]]:
                    return False

            if s[i] not in s_p:
                s_p[s[i]] = p[i]
            else:
                if p[i] != s_p[s[i]]:
                    return False 
        return True
            


        