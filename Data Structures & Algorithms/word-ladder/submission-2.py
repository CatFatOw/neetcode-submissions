import string
from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        letters = list(string.ascii_lowercase)

        def bfs(beginWord, endWord, visited, wordList):
            queue = deque([beginWord])
            visited.add(beginWord)
            total = 0

            while queue:
                temp = len(queue)
                total += 1
                for _ in range(temp):
                    word = queue.popleft()
                    if word == endWord:
                        return total
                    
                   
                    

                    for i in range(len(word)):
                        for mutation in letters:
                            new_word = list(word)
                            new_word[i] = mutation
                            new_word = "".join(new_word)

                            if new_word in wordList and new_word not in visited:
                                visited.add(new_word)
                                queue.append(new_word)
            return 0
        visited = set()
        return bfs(beginWord, endWord, visited, wordList)
                                


