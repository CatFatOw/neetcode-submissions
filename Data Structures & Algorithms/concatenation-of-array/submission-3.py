class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        nums:arr, length n 

        create ans :arr length 2n 
        ans[i] = nums[i]
        """
        
        ans = []
        length = len(nums)

        for i in range(2*len(nums)):
            number = i % length 
            ans.append(nums[number])
        return ans