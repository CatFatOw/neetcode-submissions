class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        happy_child = 0
        idx = 0

        for j in range(len(s)):
            if idx < len(g) and s[j] >= g[idx]:
                happy_child += 1
                idx += 1
        
        return happy_child
            
        