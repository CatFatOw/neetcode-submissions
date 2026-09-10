class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Absolute path in unix: always begins with / 
        transform this into a simplified canonical path


        .  current directory
        ..  parent direcoty 
        // and /// are treated as / 
        any sequence of parents are valid directory/file names 


        RULES: 
        must start with / 
        must be separated with 1 / 
        not end with a / unless its a root
        not have . or .. used 

        EXAMPLE: 
        path = "/neetcode/practice//...///../courses"
        output = "/neetcode/practice/courses"


        APPORACH:
        we first split by "/"

        if its empty, we can ignore. if its a word we append it to the stack
        if .. we pop it finally then we combine with "/"
        """

        stack = []
       

        split_path = path.split("/")
     
        for dirr in split_path:
            if dirr == ".." and stack:
                stack.pop()
            elif dirr == ".":
                continue

            elif dirr != "" and dirr != "..":
                stack.append(dirr)
            
                
        return "/" +  "/".join(stack)
      




        