class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        1. Scan left to right.
2. Push indices of '(' onto a stack.
3. If you see ')':
   - if stack has an unmatched '(', pop it
   - otherwise, this ')' is invalid, mark its index for removal
4. After the scan, anything still in the stack is an unmatched '('
5. Build the final string while skipping all marked indices 
        """

        stack = []
        removed = set()
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    removed.add(i)
        
        out = ""
        for i in range(len(s)):
            if i not in stack and i not in removed:
                out += s[i]
        return out 

        