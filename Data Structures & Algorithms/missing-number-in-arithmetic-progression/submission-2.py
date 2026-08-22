class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        """
        arr: arrau 
        the values of arr[i+1] - arr[i] are equal for all i 

        a value of arr was removed and was not the first or last value.

        return this removed value

        APPROACH:

        1. sort the array
        2. since the first and last values were not removed, we can find the difference between them
        3. the expected value is arr[mid] + diff and we compare that :D 
        """
        left = 0
        right = len(arr)-1
        arr.sort()
        # common difference
        diff = (arr[-1] - arr[0]) // len(arr)

        while left <= right:
            mid = (left+right)//2
            # standard def of arthemetric progression
            expected = arr[0] + (mid * diff)
  
            if arr[mid] == expected:
                left = mid + 1
            
            else:
                right = mid -1
        return arr[0] + left * diff