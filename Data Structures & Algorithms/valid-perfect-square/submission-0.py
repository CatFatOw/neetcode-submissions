class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        positive number nums:
        return True is nums is a perfect square else fasle


        APRAOCH:

        we can gerate numbers from 1 to nums. if there exists a nums | x * x == nums then true
        """
        
        left = 0
        right = num
        while left <= right:
            mid = (left+right)//2
            if mid*mid == num:
                return True 
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
        