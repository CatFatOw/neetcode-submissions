from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Use a hashmap to keep track of the word frequency
        If the hashmap is the same, then they are anagram

        main challege: finding everything

        Lets first do a O(n^2) solution
        """
        result = []
        mapping_list = []

        for word_idx in range(len(strs)):
            mapping = defaultdict(int)
            word = strs[word_idx]
            for char in word:
                mapping[char] += 1
            mapping_list.append(mapping)

        for i in range(len(strs)):
            valid = [strs[i]]
            for j in range(len(strs)):
                if i != j and mapping_list[i] == mapping_list[j]:
                    valid.append(strs[j])
            valid.sort()
            if valid not in result:
                result.append(valid)

        return result
