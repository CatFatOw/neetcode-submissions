class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def violates(s):
            """Vilates iff leading 0"""
            for segment in s.split("."):
                if segment[0] == "0" and len(segment) > 1:
                    return True 
                if int(segment) > 255:
                    return True
            return False
        
        def backtrack(index, arr):
            # 4 valid segments
            if len(arr) == 4:
                if index == len(s):
                    result.append(".".join(arr.copy()))
                return None 
        

            # each IP address has 3 valid "segements of digits"
            for i in range(1, 4):
                length = index + i
                if length > len(s):
                    continue 
                    
                if violates(s[index:length]):
                    continue 
                
                arr.append(s[index:length])
                backtrack(length, arr)
                arr.pop()

        backtrack(0, [])
        return result



        