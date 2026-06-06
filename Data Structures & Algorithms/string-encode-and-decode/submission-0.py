class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            length = len(word)
            output += f"{length}#{word}"
        return output


        

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            digit = ""
        
            
            while s[i] != "#":
                digit += s[i]
                i+=1
            length = int(digit)
            word = s[i + 1:i + 1 + length]
            output.append(word)
            i = i + 1 + length
        return output




