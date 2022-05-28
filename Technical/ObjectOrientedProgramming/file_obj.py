# File objects

from cgi import test
import os
os.getcwd()
os.listdir('.')

# for some reason relative path doesn't work, so using absolute path
path = "D:\GitHub\CodingChallenges\Technical\ObjectOrientedProgramming"
testFile = path + '\\test.txt'
testFile2 = path + '\\test2.txt'
testFile3 = path + '\\test_copy.txt'
print('file path:', testFile)

# using context manager
# the benefit is we work with data within this block of code,
# but once we exit it, it exit for file for us as well
with open(testFile, 'r') as f:
    # big files is better to use readlines(), instead of read()

    # this is efficient, b/c it's not reading all the contents at once
    # but reading a line at a time
    '''
    for line in f:
        print(line, end='')
    '''

    # f_contents = f.read()
    # f_contents = f.readline()
    '''
    f_contents = f.read(5)
    print(f_contents, end='')
    '''

    size_to_read = 10
    f_contents = f.read(size_to_read)

    print(f.tell()) # shows the current position at the file in the reading (meaning 10th character location)
    f.seek(0) # sets the position back to the beginning

    # this repeats until the file return an empty string
    while len(f_contents) > 0:
        print(f_contents, end='***')
        f_contents = f.read(size_to_read)


# writing file - w = overwriting to a file
# if you don't want to overwrite it, use 'a' = appending
with open(testFile2, 'w') as f:
    f.write('Test')
    f.seek(0) # setting back to the original position, it can be confusing
    f.write('R')

# open('path\file name','r=read, w=write, a=appending, r+=read+write')
f = open(testFile, 'r')

print('file name', f.name)
print('file mode: ', f.mode) # prints out r, because we opened with reading


# we also need to CLOSE the file, if you don't want to end up with junks
f.close()

# reading and write at the same time
# creating a copy
with open(testFile, 'r') as rf:
    with open(testFile3, 'w') as wf:
        for line in rf:
            wf.write(line)

# in order to copy imgs, we need to work with binaries (aka bytes.)
'''
with open('bronx.jpg', 'rb') as rf:
    with open('bronx_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)
'''

# using specific chunk size
'''
with open(testFile, 'r') as rf:
    with open(testFile3, 'w') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
'''