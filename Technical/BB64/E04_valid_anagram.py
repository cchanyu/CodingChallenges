def isAnagram(self, s, t):
    if len(s) != len(t):
        return False
    
    Cs = Counter(s)
    Ct = Counter(t)

    for c in Cs:
        if Cs[c] != Ct[c]:
            return False
    return True