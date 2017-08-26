import os
import BagOfWords
import lcsClass
from matrix import matsetter
import fingerprint

# enter the path of the directory in which all text files to be tested are present

path = str(input())
try:
    assert os.path.exists(path)
except AssertionError:
    print("Given path does not exist")
else:
    l = []
    fin = []
    b = []

    # gets all files in the given directory into a list

    m = [i for i in os.listdir(path) if i.endswith(".txt")]
    if "output.txt" in m:
        m.remove("output.txt")
    os.chdir(path)
    for filename in m:
        f = open(filename, "r")

        # create an object of lcs class

        f1 = lcsClass.Lcs(f, filename)

        # creates a finger print object for the given file

        o = fingerprint.fingerprint(filename)


        # creates a Bag Of Words object for the given file

        x = BagOfWords.BagOfWords(filename)

        # appends each object to their respective lists

        b.append(x)
        fin.append(o)
        l.append(f1)
    print("Using LCS method\n")
    matsetter(l)
    print("\nUsing Finger printing method")
    matsetter(fin)
    print("\nUsing Bag of Words method")
    matsetter(b)
    print("\n Note: A '-1' in the matrix indicates while comparison one or both of the files were found empty")





