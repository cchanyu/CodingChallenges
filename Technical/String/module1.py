print("This will always print")

def main():
    # When this runs, __name__ looks for __main__ first
    print ("1st Module's name: {}".format(__name__))

if __name__ == '__main__':
    main()
    print("Run Directly")
else:
    print("Run from Import")