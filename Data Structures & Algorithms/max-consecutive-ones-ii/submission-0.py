class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        left = 0
        flipped_count = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                curr += 1
            else:
                flipped_count += 1
                curr += 1

            while flipped_count > 1:
                if nums[left] == 1:
                    curr -=1 
                elif nums[left] == 0:
                    flipped_count -=1
                    curr -= 1
                left += 1
            ans = max(ans, curr)
        return ans


                

        