import sys # allows access to command line

vocab = {} # dict to store frequency list

fd = open('wiki.txt', 'r') # opens the freq.txt in read mode
# for each of the lines of input

for line in fd.readlines(): # the form is the line without spacing
    form = line.strip() # if we haven't seen it yet,set the frequency count to 0
    if form not in vocab:
        vocab[form] = 0
    vocab[form] = vocab[form] + 1

for line in sys.stdin.readlines(): # takes the system input    
    words=line.split(' ') #stores in variable "words", the split input
    for c in words:# basic loop
        if c in vocab:
            sys.stdout.write(c + ' ') #export to standard output 
        else:
            sys.stdout.write('*' + c + ' ') #export to standard output + *
