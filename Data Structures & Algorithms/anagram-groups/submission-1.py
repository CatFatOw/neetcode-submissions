from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Use a hashmap to keep track of the word frequency
        If the hashmap is the same, then they are anagram

        main challege: finding everything

        Lets first do a O(n^2) solution
        """
        groupings = defaultdict(list)

        for word in strs:

            chars = [0] * 26
            for char in word:
                chars[ord(char) - ord("a")] += 1

            key = tuple(chars)
            groupings[key].append(word)
            
        return list(groupings.values())


            