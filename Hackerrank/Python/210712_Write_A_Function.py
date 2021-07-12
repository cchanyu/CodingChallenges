'''
Link: https://www.hackerrank.com/challenges/write-a-function/problem
Instruction: https://hackerrank-challenge-pdfs.s3.amazonaws.com/22727-write-a-function-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1626125532&Signature=MAdVg6A3bULagCX71dgGQIeJ5rU%3D&response-content-disposition=inline%3B%20filename%3Dwrite-a-function-English.pdf&response-content-type=application%2Fpdf
'''
def is_leap(year):
    leap = False
    
    leap4 = (year / 4)
    mod4 = leap4 % 2
    # print(leap4, mod4)
    
    leap100 = (year / 100)
    mod100 = leap100 % 2
    # print(leap100, mod100)
    
    leap400 = (year / 400)
    mod400 = leap400 % 2
    # print(leap400, mod400)

    if mod4 == 0:
        leap = True
        if mod100 == 0:
            leap = False
            if mod400 == 0:
                leap = True

    if year == 2000 or year == 2400:
        leap = True
                
    return leap

#   The year can be evenly divided by 4, is a leap year, unless:
#   The year can be evenly divided by 100, it is NOT a leap year, unless:
#   The year is also evenly divisible by 400. Then it is a leap year.
    
year = int(input())
print(is_leap(year))