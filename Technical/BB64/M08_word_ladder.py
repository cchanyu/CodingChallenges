import collections


def ladderLength(self, beginWord, endWord, wordList):
    if endWord in wordList:
        return 0
    
    neighbor = collections.defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for match in range(len(word)):
            pattern = word[:match] + "*" + word[match + 1:]
            neighbor[pattern].append(word)

    visit = set([beginWord])
    q = collections.deque([beginWord])
    res = 1
    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return res
            for match in range(len(word)):
                pattern = word[:match] + "*" + word[match + 1:]
                for neighborWord in neighbor[pattern]:
                    if neighborWord not in visit:
                        visit.add(neighborWord)
                        q.append(neighborWord)
        res += 1

    return 0

'''
input: begin: hit, end: cog
array of wordlist: [hot,dot,dog,lot,log,cog]

intuition: since one word can change at a time, have to create a connections
hit -> either Xit, hXt, hiX
Xit connects to  
hXt connects to hot
hiX connects to 

This is like a Graph/Tree problem.

O(n*m^2)
'''