class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        hmap = defaultdict(list)
        change = 1

        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                hmap[pattern].append(word)
        
        queue = deque()
        queue.append(beginWord)
        visit = set()
        visit.add(beginWord)

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return change
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for i in hmap[pattern]:
                        if i not in visit:
                            visit.add(i)
                            queue.append(i)
            
            change += 1
        
        return 0
