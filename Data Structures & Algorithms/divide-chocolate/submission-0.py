class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        
        # Lets do binary search on the indicies 
        left = min(sweetness)
        right = sum(sweetness)
        total_sum = sum(sweetness)
        ans = left
        while left <= right:
            temp = 0
            mid = (left + right) // 2
            pieces = 0

            for i in  range(0, len(sweetness)):
                temp += sweetness[i]
                if temp >= mid:
                    pieces += 1
                    temp = 0

            if pieces >=k+1:
                ans =  mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
            
            
