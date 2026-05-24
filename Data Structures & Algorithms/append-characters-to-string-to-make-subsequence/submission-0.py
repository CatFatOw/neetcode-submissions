class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        if t in s:
            return 0
            
        result = 0
        s_ptr = 0
        t_ptr = 0

        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
                t_ptr += 1
            else:
                s_ptr += 1
        
        result += len(t) - t_ptr
        return result
                
        