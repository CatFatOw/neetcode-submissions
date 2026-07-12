class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = {
        str(i + 1):chr(ord('A') + i)
        for i in range(26)
    }
        memo = {}
        def dp(idx):
            if idx == len(s):
                return 1

            if s[idx] == "0":
                return 0
            if idx in memo:
                return memo[idx]
            # we can either take or not take 
            ways = dp(idx+1)
            if idx + 1 < len(s) and 10 <= int(s[idx:idx+2]) <= 26:
                take_two = dp(idx+2)
                total = ways+take_two
            else:
                total = ways
            memo[idx] = total
            return total

        return dp(0)

        