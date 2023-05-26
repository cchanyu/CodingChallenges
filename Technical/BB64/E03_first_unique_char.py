def firstUniqChar(self, s):
    c = Counter(s)
    for i,v in enumerate(s):
        if c[v] == 1:
            return i # position of the first uniq char
    return -1 # if no unique char, return -1