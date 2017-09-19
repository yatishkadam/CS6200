All the tasks are coded in Python, version 2.7
_____________________________________________________________________________________________________________________
Libraries needed:

from collections import Counter
import os.path
import fnmatch
import math
import re
import operator
_____________________________________________________________________________________________________________________

FILE LISTS

 LuceneQuery.txt 
	-> Contains the output from running the query in Q.txt file using Lucene
		4 tables. 1 for each query

 BM25Query.txt
	-> Contains the output from running the query in Q.txt file using BM25
		4 tables. 1 for each query


 HW4.Java
	-> the Lucene file
		run as specified in the HW4.pdf and provide the nessasary paths as required when running the file
 BM25.py
	-> the Python file that implements the BM25 model
		To run this file
			-> Make changes to the paths in the files as specified in the file.
				(if needed use the files in the HW3.rar file provided) 
			-> call the main function with the query document as the parameter.
invertedindex.py
	-> Python file to get the inverted index
 
implementation.pdf & implementation_BM.pdf
	-> explains the documentation which is used by me to implement BM25

 Task5.pdf
	-> explains the comparison between Lucene and BM25
 HW3.rar
	-> contains the files that can be used as an input to the BM25 and Lucene files
_____________________________________________________________________________________________________________________
Sources of Information:

1. https://docs.python.org/2/library/functions.html
2. http://www.cs.cornell.edu/courses/cs4300/2013fa/lectures/retrieval-models-2-4pp.pdf