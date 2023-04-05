'''
avoid plagiarism
- detect 2 most likely books that might have plagiarism:
    looking for books with longest shared common section of text

we can skip characters, as long as its substrings
Ex: Learning
yes: Learn, Earn, Earning
not: Le g, A n, Ear n    
'''

'''
video suggest:
naive solution is to come up with every single solution
and compare the two
'''
find_longest_substring(a,b,0,0)

def find_longest_substring(str1, str2, idx1 = 0, idx2 = 0, memo=None):
    if memo is None: memo = [[-1] * len(str2)] * len(str1)
    if idx1 == len(str1) or idx2 == len(str2): return 0
    if memo[idx1][idx2] != -1: return memo
    possibility1 = find_longest_substring(str1, str2, idx1+1, idx2)
    possibility2 = find_longest_substring(str1, str2, idx1, idx2+1)
    if str1[idx1] == str2[idx2]:
        possibility3 = find_longest_substring(str1, str2, idx1+1, idx2+1) + 1
    memo[idx1][idx2] = max(possibility1, possibility2, possibility3) # poss3 if applicable
    return memo[idx1][idx2]

'''
runtime: O of N of N
'''