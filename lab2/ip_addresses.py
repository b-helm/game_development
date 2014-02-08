#Benjamin Helm, 2/13/2014
#Comp 23 Lab 2

def main():
    """ Prints out all the possible IPv4 addresses """
    for a in range (0,256):
        for b in range (0,256):
            for c in range (0,256):
                for d in range (0,256):
                    print str(a) + "." + str(b) + "." + \
                    str(c) + "." + str(d)

if __name__ == "__main__":
    main()
