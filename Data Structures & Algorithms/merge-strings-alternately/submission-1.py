class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1 = 0
        ptr2 = 0
        result = ""
        counter = 0

        while ptr1 < len(word1) and ptr2 < len(word2):
            if counter % 2 == 0:
                result += word1[ptr1]
                ptr1 += 1
            else:
                result += word2[ptr2]
                ptr2 += 1
            counter += 1


        while ptr1 < len(word1):
            result += word1[ptr1]
            ptr1 += 1
        while ptr2 < len(word2):
            result += word2[ptr2]
            ptr2 += 1
        return result

        