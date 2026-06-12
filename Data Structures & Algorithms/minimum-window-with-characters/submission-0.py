from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_mapping = defaultdict(int)
        s_mapping = defaultdict(int)
        for char in t:
            t_mapping[char] += 1
        
        need = len(t_mapping)
        curr = 0
        output = []
        left= 0
        length = float("inf")
        ans = []


        for right in range(len(s)):
            s_mapping[s[right]] += 1
            output.append(s[right])
            if s[right] in t_mapping and s_mapping[s[right]] == t_mapping[s[right]]:
                curr += 1
            
            while curr == need:
                if len(output) < length:
                    ans = list(output)
                    length = len(output)
                    
                s_mapping[s[left]] -=1
                if s_mapping[s[left]] <= 0:
                    s_mapping.pop(s[left])
                if s[left] in t_mapping and s_mapping[s[left]] < t_mapping[s[left]]:
                    curr -= 1
                output.pop(0)
                left += 1

        return "".join(ans)
        
            
            


            





