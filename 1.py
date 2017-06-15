#function prints, the number of lines, words, and characters in the file
def stats(filename):
    numlines = 0
    words = 0
    chars = 0
    with open(filename,'r') as fil:
        for lin in fil:
            wordslit=lin.split()
            numlines+=1
            words+=len(wordslit)
            chars+=len(lin)
    print("Line Count:%i\nWords Count:%i\nCharacters Count:%i" % (numlines, words, chars))

stats('sample.txt')
