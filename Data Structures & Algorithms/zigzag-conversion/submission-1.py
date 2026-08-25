class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        given a normal string and num rows

        copnvert it to a zigzag pattern

        go down, thenb diagonally and repeat 

        APPORACH:
        have a counter. if counter < numRows: add it to the same correcponding row, otherwise move to the next array and move it in from bottom left to right

        [    ]
        [    ]
        [    ]

        we iterate, each time we iterate we increment row index by 1 until it hits numRows. Then we reverse the direction with row_ix -= 1 until it hits 0
        """
        result = [[] for _ in range(numRows)]
        row_idx = 0
        reverse=False
        for i in range(len(s)):
            
            
            result[row_idx].append(s[i])
            
            if row_idx == numRows-1:
                reverse=True
            if row_idx == 0:
                reverse = False
            
            if reverse:
                row_idx -= 1
            else:
                row_idx += 1

        ans = ""        
        for x in result:
            #print("".join(x))
            ans += "".join(x)
        return ans
        

