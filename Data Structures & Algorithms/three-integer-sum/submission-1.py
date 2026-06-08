from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
     
        mapping = defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    val = -(nums[i] + nums[j])
                    mapping[val].append([i, j])
    
                    
        result = []
        for k in range(len(nums)):
            val = nums[k]
            if val in mapping:
                for x, y in mapping[val]:
                    if k != x and k != y:
                        temp = [nums[x], nums[y], nums[k]]
                        result.append(sorted(temp))
        answer = []
        for arr in result:
            if arr not in answer:
                answer.append(arr)
        return answer

        