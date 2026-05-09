from collections import defaultdict
class Solution:
    def countElements(self, arr: List[int]) -> int:
        mapping = defaultdict(int)
        ans = 0
        for num in arr:
            mapping[num] += 1
        print(mapping)
        for num in set(arr):
            if num + 1 in mapping:
                ans += mapping[num]
        return ans
