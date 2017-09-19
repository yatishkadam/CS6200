import os
import operator
import re

In_index = {}          # InvertedIndexer for Unigrams
Bigrams = {}         # InvertedIndexer for Bigrams
Trigrams = {}         # InvertedIndexer for Trigrams
TF_uni = {}         # Term Frequency for Unigrams
TF_Bi = {}        # Term Frequency for Bigrams
TF_Tri = {}        # Term Frequency for Trigrams
# Give path of the directory containing the text files
path = 'C:\Users\yatish\Desktop\IR\hw3\parsedtextfiles'

#generates name of the file
def make_new_name(textname):
    pat = re.search(r'.txt', textname)
    new_name = textname[:pat.start()]
    return new_name

def InvertedIndex(path):
    for filename in os.listdir(path):
        f = open(path + '\\' + filename, 'r+')
        s = f.read()
        new_s = s.split()
        filename=make_new_name(filename)
        # generate Unigrams
        for i in new_s:
            if i not in In_index:
                In_index[i] = {filename: 1}
            else:
                if filename not in In_index[i]:
                    In_index[i].update({filename: 1})
                else:
                    In_index[i][filename] += 1

        # generate Bigrams
        for i in range(0, len(new_s) - 1):
            bi = new_s[i] + " " + new_s[i + 1]
            if bi not in Bigrams:
                Bigrams[bi] = {filename: 1}
            else:
                if filename not in Bigrams[bi]:
                    Bigrams[bi].update({filename : 1})
                else:
                    Bigrams[bi][filename] += 1

        # generate Trigrams
        for i in range(0, len(new_s) - 2):
            ti = new_s[i] + " " + new_s[i + 1] + " " + new_s[i + 2]
            if ti not in Trigrams:
                Trigrams[ti] = {filename: 1}
            else:
                if filename not in Trigrams[ti]:
                    Trigrams[ti].update({filename: 1})
                else:
                    Trigrams[ti][filename] += 1
        f.close()

def getsum(dict):
    sum = 0
    for i in dict:
        sum += dict[i]
    return sum

def get_docs(dict):
    docs_var = ""
    for i in dict:
        docs_var += " " + str(i)
    return docs_var

def ngram_tf_files():
    for i in In_index:
        TF_uni[i] = getsum(In_index[i])

    for i in Bigrams:
        TF_Bi[i] = getsum(Bigrams[i])

    for i in Trigrams:
        TF_Tri[i] = getsum(Trigrams[i])

    f1 = open("UNIGRAM-TF.txt", "w+")
    var = sorted(TF_uni.items(), key=lambda x: (-x[1], x[0]))
    for y in var:
        f1.write(str(y) + "\n")
    f1.close()

    f1 = open("BIGRAM-TF.txt", "w+")
    var = sorted(TF_Bi.items(), key=lambda x: (-x[1], x[0]))
    for y in var:
        f1.write(str(y) + "\n")
    f1.close()

    f1 = open("TRIGRAM-TF.txt", "w+")
    var = sorted(TF_Tri.items(), key=lambda x: (-x[1], x[0]))
    for y in var:
        f1.write(str(y) + "\n")
    f1.close()



def make_ngram_tables():
    f = open('UNIGRAM-DF.txt', 'w')
    for i in sorted(In_index, key=operator.itemgetter(0)):
        term = i
        doc = get_docs(In_index[i])
        docf = len(In_index[i])
        f.write(str(term + "--->" + doc + " " + str(docf) + "\n"))
    f.close()

    f = open('BIGRAM-DF.txt', 'w')
    for i in sorted(Bigrams, key=operator.itemgetter(0)):
        term = i
        doc = get_docs(Bigrams[i])
        docf = len(Bigrams[i])
        f.write(str(term + "--->" + doc + " " + str(docf) + "\n"))
    f.close()

    f = open('TRIGRAM-DF.txt', 'w')
    for i in sorted(Trigrams, key=operator.itemgetter(0)):
        term = i
        doc = get_docs(Trigrams[i])
        docf = len(Trigrams[i])
        f.write(str(term + "--->" + doc + " " + str(docf) + "\n"))
    f.close()


def main():
    InvertedIndex(path)
    ngram_tf_files()
    make_ngram_tables()


main()