from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for word in strs:
            mapping[tuple(sorted(word))].append(word)
        result = []
        for value in mapping.values():
            result.append(value)
        return result

        