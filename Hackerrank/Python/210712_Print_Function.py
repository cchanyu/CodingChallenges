'''
Link: https://www.hackerrank.com/challenges/python-print/problem
Instruction: https://hackerrank-challenge-pdfs.s3.amazonaws.com/8026-python-print-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1626125967&Signature=1lXAiwp5ucSpfigpox3NOEsbafI%3D&response-content-disposition=inline%3B%20filename%3Dpython-print-English.pdf&response-content-type=application%2Fpdf
'''
if __name__ == '__main__':
    n = int(input())
    i = 0
    ans = []
    ans1 = ""
    
    for i in range(n):
        ans.append(str(i+1))
        i = i + 1

    ans1 = "".join(ans)
    print(ans1)