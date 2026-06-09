
class Solution:

    def is_palindrome(self, s, left, right):
        while left <= right:
            if s[left] != s[right]:
                return False 
            left += 1
            right -= 1
        return True 
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        deleted = False

        while left <= right:
            # Get rid of alnum characters
            while not s[left].isalnum() and left < right:
                left += 1

            while not s[right].isalnum() and left < right:
                right -= 1

            if s[left] == s[right]:
                right -= 1
                left += 1
            else:
                return self.is_palindrome(s, left+1, right) or self.is_palindrome(s, left, right-1)
        return True