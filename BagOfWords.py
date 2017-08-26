import re, math


class BagOfWords(object):
    def __init__(self, f):
        self.d = {}
        self.filename = f

        # opens the file and stores it instance variable f

        self.f = open(self.filename, "r")

        # function call to insert words

        self.insertWords()

    def insertWords(self):
        for line in self.f:

            # stores all the words converting all of them to lower case and removes all special characters

            for word in re.findall(r'\w+', line):
                if word in self.d:
                    self.d[word.lower()] += 1
                else:
                    self.d[word.lower()] = 1

    # prints the name of the flle for which object is created

    def __str__(self):
        return str(self.filename)

    # calculates the mod of a given file

    def mod(self):
        prod = 0
        for j in self.d:
            prod += (self.d[j])**2
        return math.sqrt(prod)

    # compares the two given files and returns plagiarism percrnt

    def compare(self, other):
        dotprod = 0
        for i in self.d.keys():
            try:
                dotprod = dotprod + (self.d[i]*other.d[i])
            except KeyError:
                continue

        # returns -1 if one or both of he files given for comparison are empty

        if self.mod() == 0 or other.mod() == 0:
            return int(-1)
        else:
            return dotprod/(self.mod()*other.mod()) * 100

