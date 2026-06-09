class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0

        for i in range(len(height)):
            left = max(height[:i+1])
            right = max(height[i:])

            trapped_water = (min(left, right) - height[i]) 
            
            ans += trapped_water 
            
        return ans
        