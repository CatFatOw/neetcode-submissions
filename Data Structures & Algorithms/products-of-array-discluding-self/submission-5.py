class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums: arr 
        return output where output[i] where output[i] is product of all elements erxcept nums[i]

        APPROACH:
        we do a two pointer apporach, we decrement one and increment one starting at index i 


        EXAMPLE 
        [1,2,4,6]
        
        PREFIX:
        [1, 1, 2, 8]
        ↑
        placeholder

        SUFFIX:
        [48, 24, 6, 1]
                ↑
            placeholder

        result[0] =  suffix[0] * prefix[i+1] = 48
        result[1] = suffix[1] * prefix[1+1] = 2 * 24

        """

        prefix = [1] * (len(nums)+1)
        suffix = [1] * (len(nums)+1)
        
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]


        result = []
        for i in range(len(prefix)-1):
            result.append(prefix[i] * suffix[i+1])
        
        return result


        