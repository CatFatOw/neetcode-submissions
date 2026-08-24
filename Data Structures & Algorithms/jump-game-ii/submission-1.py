class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        nums[i] represent the maximum length of a jump towards the right from index i. if at index i we can jump to i+j where j <= nums[i]

        return min # of jumps to reach the last position

        APPROACH: DP

        base case:
        if i == le(nums):
            return 0
        
        use a for loop ot specify the numbers of jumps

        """

        memo = {}
        def dp(i):
            if i == len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]
            
            min_jumps = float("inf")
            for j in range(1, nums[i]+1):
                if i + j < len(nums):
                    jumps = 1 + dp(i+j)
                    min_jumps = min(min_jumps, jumps)
            memo[i] = min_jumps
            return min_jumps
        return dp(0)

                
        