def isPalindrome(self, x):
    if x < 0:
        return False
    
    list = []

    while x >= 10:
        list.append(x % 10)
        x //= 10
    list.append(x)

    for i in range(len(list) // 2):
        if list[i] != list[len(list)-i-1]:
            return False
    return True

# Convert to String, then compare
def isPalindrome(self, x):
    x1 = str(x)
    x2 = x1[::-1]
    return (x1 == x2)

'''
x: 121
output: true

x: -121
output: false (121-)
'''