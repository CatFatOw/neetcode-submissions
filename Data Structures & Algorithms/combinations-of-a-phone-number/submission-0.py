class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        temp = []
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if not digits:
            return []

        def backtrack(i):
            if i == len(digits):
                copy = "".join(temp)
                result.append(copy)
                return 
            current_digit = digits[i]
            for number in mapping[current_digit] :
                temp.append(number)
                backtrack(i+1)
                temp.pop()
        backtrack(0)
        return result


        