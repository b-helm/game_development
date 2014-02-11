#Benjamin Helm, 2/13/2014
#Comp 23 Lab 2

import sys

def main():
    """ prints the word frequency of the file named on the command line """
    try:
        f = open(sys.argv[1]).read()
    except IOError:
        print "Invalid File"
        sys.exit()

    word_list = {}
    word_count = 0
    for word in f.split():
        word_count += 1
        if word in word_list:
            word_list[word.lower()] += 1
        else:
            word_list[word.lower()] = 1

    for key, value in word_list.items():
        print key + " " + str(value)
    print "There are " + str(word_count) + " words in the file."

if __name__ == "__main__":
    main()
