# coding=utf-8

##################################################
## Begin KEYLIST script.                        ##
##################################################
## This is a program to get a basic list of key ##
## terms from a target corpus (TC) by comparing ##
## the frequencies of TC words to those of a    ##
## reference corpus (RC).                       ##
##################################################
## NOTE: The natural language toolkit only      ##
## functions with ASCII characters. Any file to ##
## be used as either RC or TC should be a text  ##
## (.txt) file consisting entirely of ASCII     ##
## characters. To do a quick and dirty cleanup  ##
## of a non-ASCII containing file, do a RegEx-  ##
## enabled search for [^\x00-\x7F] and replace  ##
## all such characters with a space or with an  ##
## indicator character such as an underscore or ##
## backslash.                                   ##
##################################################
## Written by Aly M.W. Sevre                    ##
## (c) 2015 SMATOOS, Inc.                       ##
##################################################



# Import necessary modules
import nltk

def readfile(filename):
    f = open(filename)
    contents = f.read()
    f.close()
    return contents

# Get reference info
rstuff = readfile('brown-all.txt')

rtokens = nltk.word_tokenize(rstuff)
rtext = nltk.Text(rtokens)
rtext = [w for w in rtext if w.isalpha()]

# Get frequency list of the Top 2000 words in the reference list (rtop2k)
rfreq = nltk.FreqDist(rtext)
print("Reference frequency list: %s" % rfreq)
rtop2k = rfreq.most_common(2000)
exclusion_words = []
for r in rtop2k:
    exclusion_words.append(r[0])
print("Top 2000 list: %s" % rtop2k)

# Get target info
tstuff = readfile('target_corpus.txt')

ttokens = nltk.word_tokenize(tstuff)
ttext = nltk.Text(ttokens)
ttext = [w for w in ttext if w.isalpha()]

# Get frequency list of all the target info (tfreq)
tfreq = nltk.FreqDist(ttext)
print("Target frequency list: %s" % tfreq)


# Generate list of target words (klist) by excluding rtop2k from tfreq
klist = []
for w in tfreq:
    if w not in exclusion_words:
        klist.append(w)
print("Key word list: %s" % klist)



##################################################
## End KEYLIST script.                          ##
##################################################