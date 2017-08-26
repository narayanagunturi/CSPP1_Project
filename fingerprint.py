import os, re

class fingerprint(object):
    def __init__(self,f):

        # opens the file, and stores it in an instance variable

        self.filename = f
        self.k = open(f, "r")
        self.l = []

        # stores the entire file in an instance variable s without any special characters

        for line in self.k:
            for word in re.findall(r'\w+',line):
                self.l.append(word.lower().strip("_"))
        self.s = ''.join(self.l)

        # function call to create a hash list for the file

        self.shash = self.hash()

    # creates a hash list for the file

    def hash(self):
        m = []
        for i in range(len(self.s)-4):
            y = self.s[i:i+5]
            sum = 0
            for j in range(5):
                sum += (ord(y[j]) * pow(5, j)) % 10007
            m.append(sum)
        return m

    # compares the hash lists of two files and returns plagiarism percent between the two files

    def compare(self, other):
        count = 0
        k = set(self.shash)
        k = list(k)
        for char in k:
            l = [i for i,x in enumerate(other.shash) if x == char]
            count = count + len(l)

        # returns -1 if one or both of the files given for comparison are empty

        if self.shash == [] or other.shash == []:
            return int(-1)
        else:
            return (count * 2) / (len(k) + len(other.shash)) * 100




