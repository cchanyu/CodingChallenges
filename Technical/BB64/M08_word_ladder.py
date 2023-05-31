def ladderLength(self, beginWord, endWord, wordList):
    ans = 0

    wordList = set(wordList)
    
    return ans

'''
input: begin: hit, end: cog
array of wordlist: [hot,dot,dog,lot,log,cog]

intuition: since one word can change at a time, have to create a connections
hit -> either Xit, hXt, hiX
Xit connects to  
hXt connects to hot
hiX connects to 

This is like a Graph/Tree problem.

'''