class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2":["a", "b", "c"], "3": ["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m","n", "o"], "7":["p","q", "r", "s"], "8":["t", "u", "v"], "9":["w","x","y", "z"]}

        result = []
        if len(digits) == 0:
            return result

        def backtrack(idx, arr):
            if idx == len(digits):
                result.append("".join(arr.copy()))
                return 
            
            
            for char in mapping[digits[idx]]:
                arr.append(char)
                backtrack(idx+1,arr)
                arr.pop()
        backtrack(0, [])
        return result
        