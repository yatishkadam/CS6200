from collections import Counter
import os.path
import fnmatch
import math
import re
import operator

#! Ni is the # of docs containing term i
Index={}
Ni={}
f=open('UNIGRAM-DF.txt','r+') #provide the Path of the file UNIGRAM-DF.txt
                              # obtained from running invertedindex.py in HW3
content = f.readlines()
for line in content:
    x=line.split()
    Ni.update({x[0]:x[-1]})
    Index.update({x[0]:x[1:-1]})
f.close()

def getni(term):
    return Ni[term]
#getni('gasperi')


#! N is the total # of docs in the collection
N=1000  #changed if the number of files in the corpus
        # if changed uncomment the function call below
        #provide the path where all the parsed files are present
def totaldocs(path):
    N=len(fnmatch.filter(os.listdir(path), '*.txt'))
#totaldocs(path)


#! fi is the frequency of term i in the doc under consideration
#! dl is the document length


def fterm(term,doc):
    dic={}
    path1='C:\Users\yatish\Desktop\IR\hw3\parsedtextfiles\\' #folder path
    #provide path1 as the path for the folder which contains all the parsed html files obtained from the HW3
    path= path1 + doc +'.txt'
    f=open(path,'r+')
    content = f.read()
    x=content.split()
    count=Counter(x)
    dl=len(x)
    fterm= count[term]
    f.close()
    dic.update({'dl':dl,'fterm':fterm})
    return dic

#! avdl is the avg doc length
def avdl(path):
    global avdl
    f=open(path,'r+')
    content = f.readlines()
    count=0
    for line in content:
        x=line.split()
        count+=int(x[1][:-1])
    return (float(count)/float(N))
    f.close()
#avdl('C:\Users\yatish\Desktop\IR\BM25\UNIGRAM-TF.txt')



#CONSTANTS
b=0.75
avdl=avdl('C:\Users\yatish\Desktop\IR\BM25\UNIGRAM-TF.txt') #provide the path for UNIGRAM-TF.txt
                                                            # obtained from running invertedindex.py in HW3
k1=1.2
k2=100

def kval(term,doc):
    x=fterm(term,doc)
    #print "inside kval________________________" ,term ,doc
    #print x
    dl=x['dl']
    #print dl
    K=k1*( (1-b) + b * (dl/avdl) )
    return K

def BM25(Q,doc):
    terms=Q.split()
    BM25val=0
    c=Counter(terms)
    for term in terms:
        try:
            #value of K
            K=kval(term,doc)

            #! ri is the  # of relevant documents containing term i
               #(set to 0 if no relevancy info is known)
            ri=0
            # ! ni is the # of docs containing term i
            ni=getni(term)

            #R is the number of relevant documents for this query iff known else 0
            R=0
            ft=fterm(term,doc)
            #fi is the frequency of term i in the doc under consideration
            fi=ft['fterm']

            #qfi is the frequency of term i in the query
            qfi=c[term]
            '''print term,"________________________________________________________________",doc
            print "k=  ",K
            print 'ni=  ',ni
            print 'fi= ',fi
            print 'qfi=  ',qfi'''
            #cal BM value
            v=( ( (float(ri)+0.5) / (float(R)-float(ri)+0.5) )/( (float(ni)-float(ri)+0.5) / (float(N)-float(ni)-float(R)+float(ri)+0.5) ) )
            v1=math.log(v,2)
            v2=(((float(k1)+1)*float(fi))/(float(K)+float(fi)))
            v3=(((float(k2)+1)*float(qfi))/(float(k2)+float(qfi)))
            BMval= (v1*v2*v3)
            BM25val+=BMval
        except:
            pass
    return BM25val

def getQueryDoc(query,querynum):
    x=query.split()
    lst=[]
    d={}
    for y in x:
        for doc in Index[y]:
            lst.append(doc)
    for y in lst:
        d.update({y+'.txt':BM25(query,y)})
    sorted_x = sorted(d.items(), key=operator.itemgetter(1))
    x=sorted_x[::-1][0:100]
    count=0
    doc = ''
    bmval = ''
    for i in x:
        count+=1
        for y in i:
            if isinstance(y, str):
                doc = y
            else:
                bmval = y
        print querynum,' Q0', doc,count, bmval, 'BM25'

def main(path):
    file=open(path,'r+')
    content=file.readlines()
    content=[x.strip() for x in content]
    count=0
    for x in content:
        try:
            pat = re.search(r':',x)
            new_name = x[pat.end():]
            count+=1
            getQueryDoc(new_name,count)
        except :
            print "please make sure you have entered the query : \t\" ", x, "\"\nin the form of QueryNum : query EXAMPLE 1: Global warming"

#main('Q.txt')#Provide the path for query file