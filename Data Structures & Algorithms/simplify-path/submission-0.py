class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Transform absolute path into simplified path 

        Rules:

        . -> current direcotry 
        .. -> previous directory
        // or /// are treated as /
        any sequence of preiods that is not . or .. should be treated as valid filename/directory

        """
        directory = path.split("/")
        stack = [] 
        print(directory)

        for part in directory:
            if part == "." or part == "":
                continue 
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/" + "/".join(stack)