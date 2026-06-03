class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        temp = []

        def is_palindrome(s):
            left = 0
            right = len(s) - 1
            while left <= right:
                if s[left] != s[right]:
                    return False 
                left += 1
                right -= 1
            return True
        

        def backtrack(i):
            palindrome = []
            # Base case 
            if i == len(s):
                result.append(temp.copy())
                return 
            
            for idx in range(i, len(s)):
                palindrome.append(s[idx]) 
                # If the current is a palindrome 
                if is_palindrome("".join(palindrome)):
                    
                    temp.append("".join(palindrome))
                    backtrack(idx+1)
                    temp.pop(-1)
                
        backtrack(0)
        return result


                
        