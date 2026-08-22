class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        n coins and build a staircase with these coins

        k rows where the the ith row as exactly i coins and the last row may be incomplete 

        example n = 4 so 

        row 1: # 
        row 2: ##
        row 3: #

        return the number of complete rows that you will build 
        (in this case 2)

        APPROACH:
        we can essentailly binary sort with the index plus 1. So we can first generate this stariwell

        then we binary search and always move left and return left + 1 valid rows :D 
        """

        left = 0
        right = n
        while left <= right:
            mid = (left+right)//2
            if (mid * (mid+1))/2 <= n:
                left = mid + 1
            else:
                right = mid - 1
        return left-1


        