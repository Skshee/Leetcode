'''
Link : https://leetcode.com/problems/word-ladder/
'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def difference(str1, str2):
            diff = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    diff += 1
            return diff
        
        queue = deque()
        visit = set()
        
        queue.append([beginWord,0])
        visit.add(beginWord)
        
        while queue:
            curword, steps = queue.popleft()
            
            if curword == endWord:
                return steps + 1
            
            for word in wordList:
                if word not in visit:
                    if difference(curword, word) == 1:
                        queue.append([word, steps + 1])
                        visit.add(word)
        return 0
    # Time Complexity: O(N * M^2), where N is the number of words and M is the length of each word

    # Faster Solution : Reference : https://www.youtube.com/watch?v=h9iTnkgv05E&t=338s

    class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        neighbours = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbours[pattern].append(word)
        
        queue = deque()
        visit = set()
        queue.append(beginWord)
        visit.add(beginWord)
        res = 1

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in neighbours[pattern]:
                        if neiWord not in visit:
                            queue.append(neiWord)
                            visit.add(neiWord)
            res += 1
        return 0
    