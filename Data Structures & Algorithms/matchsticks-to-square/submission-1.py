from typing import List
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        We can backtrack
        """
        sides = [0, 0, 0, 0]
        total = sum(matchsticks)
        matchsticks.sort(reverse=True)

        def backtrack(i, sides, total):
            if i == len(matchsticks):
                if (sides[0] == total / 4) and (sides[1] == total / 4) and (sides[2] == total / 4) and (
                        sides[3] == total / 4):
                    return sum(sides) == total
                else:
                    return False
            seen = set()
            for idx in range(4):
                if sides[idx] in seen:
                    continue 
                if sides[idx] + matchsticks[i] > total / 4:
                    continue
                sides[idx] += matchsticks[i]
                seen.add(sides[idx])

                if backtrack(i + 1, sides, total):
                    return True
                sides[idx] -= matchsticks[i]
            return False

        return backtrack(0, sides, total)

