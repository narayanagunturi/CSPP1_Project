import re
from matrix import matrix
import fingerprint

class EmptyFile(Exception):
    pass

class Lcs(object):
    def __init__(self,f, filename):

        # stores the file, filename as instance variables

        self.filename = filename
        self.f = f
        self.d = []
        # stores all the words, removes all special characters
        for line in self.f:
            for word in re.findall(r'\w+', line):
                self.d.append(word.lower())

    def __str__(self):

        # printing an object will give the file name of the file stored in the object

       return str(self.filename)

    def compare(self, other):

        # Compares the data in both the files, prints the longest substring common to both files and returns the plagiarism percent
        try:
            if self.d == [] or other.d == []:
                raise EmptyFile

            # raises an exception if one or both of the files is empty

        except EmptyFile:
            print("One or both of the files in", self.filename,"and", other.filename, "is empty. Cannot compare with empty files")
        else:
            lcs = ""
            for i in range(len(self.d)):
                itemp = i
                for j in range(len(other.d)):
                    if itemp < len(self.d):
                        if self.d[itemp] == other.d[j]:
                            itemp += 1
                        else:
                            if len(lcs) < len(' '.join(self.d[i:itemp])):
                                lcs = ' '.join(self.d[i:itemp])
                            itemp = i
                            continue
                    else:
                        break
                if len(lcs) < len(' '.join(self.d[i:itemp])):
                    lcs = ' '.join(self.d[i:itemp])
                if itemp == len(self.d):
                    break
            print("longest common substring after comparing",self.filename, "with", other.filename, lcs)
            return (len(lcs) * 2 / (len(' '.join(self.d)) + len(' '.join(other.d)))) * 100