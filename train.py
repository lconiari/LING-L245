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
