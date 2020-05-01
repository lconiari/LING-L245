import sys
#import the system
vocab = {} # dict to store frequency list

# for each of the lines of input
for line in sys.stdin.readlines():
    # the form is the line without spacing
    form = line.strip()

ss = [sys.stdin.readline]
# the matrix

bigrams = {}
#declare a new matrix

vocabulary = ['#']
# Join the list with a space and then split
vocabulary += ' '.join(ss).split(' ')
vocabulary = set(vocabulary)
#iterate through matrix and print value
for token1 in vocabulary:
        for token2 in vocabulary:
                if token1 not in bigrams:
                        bigrams[token1] = {}
                if token2 not in bigrams[token1]:
                        bigrams[token1][token2] = 0
#initialize matrix by looping twice
# For each of the sentences
for s in ss:
        # Tokenise the sentence
        s = s.split(' ')
        # For each of the tokens
        for i in range(0, len(s)-1):
    # if we haven't seen it yet, set the frequency count to 0
        for line in sys.stdin.readlines(): # takes the system input
         words=line.split(' ') #stores in variable "words", the split input
        for c in words:# basic loop
                 if c in vocab:
                 sys.stdout.write(c + ' ') #export to standard output
                 else:
                 sys.stdout.write('*' + c + ' ') #export to standard output + *



