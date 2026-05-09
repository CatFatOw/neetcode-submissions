from collections import defaultdict
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        mapping = defaultdict(int)
        left = 0
        ans = 0

        for right in range(len(s)):
            mapping[s[right]] += 1

            while right - left + 1 > k:
                mapping[s[left]] -= 1
                if mapping[s[left]] <= 0:
                    mapping.pop(s[left])
                left += 1

           
            ok = True
            if len(mapping) == k:
                for freq in mapping.values():
                    if freq != 1:
                        ok = False
                        break

                if ok:
                    ans += 1
        return ans
                