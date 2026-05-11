from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        u_v = defaultdict(int)
        v_u = defaultdict(int)
        

        if len(s) != len(t):
            return False 
        
        for i in range(len(s)):
            if s[i] not in u_v:
                u_v[s[i]] = t[i]
            else:
                if t[i] != u_v[s[i]]:
                    return False
            if t[i] not in v_u:
                v_u[t[i]] = s[i]
            else:
                if s[i] != v_u[t[i]]:
                    return False 
        return True
            
            
        
        