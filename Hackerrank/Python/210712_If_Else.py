'''
Link: https://www.hackerrank.com/challenges/py-if-else/problem
Instruction: https://hackerrank-challenge-pdfs.s3.amazonaws.com/22447-py-if-else-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1626121155&Signature=%2FGcEBegcmYzdEGxyJcpgUHg1kbw%3D&response-content-disposition=inline%3B%20filename%3Dpy-if-else-English.pdf&response-content-type=application%2Fpdf
'''
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    booli = n % 2
    check1 = 2 <= n <= 5
    check2 = 6 <= n <= 20
    
    if booli == 1:
        print("Weird")
    elif booli == 0 and check1 == True:
        print("Not Weird")
    elif booli == 0 and check2 == True:
        print("Weird")
    elif booli == 0 and n >= 20:
        print("Not Weird")
