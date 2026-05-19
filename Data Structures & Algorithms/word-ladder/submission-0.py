from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        letters = [chr(i) for i in range(ord("a"), ord("z")+1)]

        def bfs(beginWord, endWord, wordList):
            queue = deque([(beginWord,1)])
            visited = set([beginWord])

            while queue:
                word, mutation = queue.popleft()
                if word == endWord:
                    return mutation

                for idx in range(len(word)):
                    for char in letters:
                        word_list = list(word)
                        word_list[idx] = char

                        result = "".join(word_list)
                        if result in wordList and result not in visited:
                            visited.add(result)
                            queue.append((result, mutation+1))
            return 0
        return bfs(beginWord, endWord, wordList)
            



        