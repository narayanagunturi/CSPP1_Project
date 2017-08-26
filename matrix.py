import fingerprint
import lcsClass


def matsetter(l):
    k = [[] for i in range(len(l) + 1)]

    # appends the string "Name of the file' in k[0][0] position

    k[0].append("Name of the file")

    # puts the names of all files in 0th row and as well in 0th column leaving k[0][0] unchanged

    for i in range(1, len(l) + 1):
        k[i].append(l[i - 1].filename)
        k[0].append(l[i - 1].filename)

    for i in range(1, len(l) + 1):
        for j in range(1, len(l) + 1):

            # avoids comparing the same files

            if i == j:
                k[i].append(None)

            # directly appends previously compared files' plagiarism percentage

            elif j < i:
                k[i].append(k[j][i])

            # compares two files and appends their plagiarism percentage

            else:
                c = l[i - 1].compare(l[j - 1])
                if c is None:
                    k[i].append(-1)
                else:
                    k[i].append(c)

    # prints the list of lists in matrix form

    matrix(k)


def matrix(l):

    # converts each element of float type to string type

    for i in range(len(l)):
        for j in range(len(l)):
            l[i][j] = str(l[i][j])
    col_lens = []

    # finds the element of longest length in a column and appends its length to col_lens list

    for j in range(len(l)):
        max = 0
        for i in range(len(l)):
            if max < len(l[i][j]):
                max = len(l[i][j])
        col_lens.append(max)

    # converts each element 'el' in col_lens list into {:'el'} and converts the list into a string, putting tab spaces between each element

    f = '\t'.join('{{:{}}}'.format(n) for n in col_lens)

    # in every column enters a tab space after the maximum length in the column

    t = [f.format(*row) for row in l]

    # joins each row with a new line i.e., the next row comes in a new line

    print('\n'.join(t))
    print("\n")



