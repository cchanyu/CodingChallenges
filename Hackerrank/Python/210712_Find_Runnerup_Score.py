'''
Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
Instruction: https://hackerrank-challenge-pdfs.s3.amazonaws.com/1374-find-second-maximum-number-in-a-list-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1626127564&Signature=F8UEE8ZvqgWSLlz733Xleny%2F%2FMI%3D&response-content-disposition=inline%3B%20filename%3Dfind-second-maximum-number-in-a-list-English.pdf&response-content-type=application%2Fpdf
'''
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    nlist = []
    ans = 0
    
    for i in arr:
        nlist.append(i)
    nlist.sort()
    
    ans = nlist[-1]
    for k in reversed(nlist):
        if ans != k:
            ans = k
            break
    
    print(ans)