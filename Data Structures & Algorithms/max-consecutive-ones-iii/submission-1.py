class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        curr_total = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                curr_total += 1
            elif nums[right] == 0 and zero_count <= k:
                curr_total += 1
                zero_count += 1
            
            while zero_count > k:
                curr_total -= 1
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            ans = max(ans, curr_total)
        return ans
            

        