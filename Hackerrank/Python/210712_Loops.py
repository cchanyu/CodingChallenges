'''
Link: https://www.hackerrank.com/challenges/python-loops/problem
Instruction: https://hackerrank-challenge-pdfs.s3.amazonaws.com/7941-python-loops-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1626122526&Signature=u9%2F9PQfIQvzdKoaDRPOkEwKTKbk%3D&response-content-disposition=inline%3B%20filename%3Dpython-loops-English.pdf&response-content-type=application%2Fpdf
'''
if __name__ == '__main__':
    n = int(input())
    i = 0
    
    if n >= 0:
        for i in range(n):
            print(i*i)
            i = i + 1