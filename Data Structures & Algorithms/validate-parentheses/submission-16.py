class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")":"(", "}":"{", "]":"["}
        stack = []

        if len(s) == 1:
            return False 
        if len(s) == 0:
            return True

        for char in s:
            if char in mapping and stack:
                complement = stack.pop()
                if complement != mapping[char]:
                    return False 
            else:
                stack.append(char)
        if not stack:
            return True 
        return False
        