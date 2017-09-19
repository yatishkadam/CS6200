All the tasks are coded in Python, version 2.7
_____________________________________________________________________________________________________________________


FILE LISTS

       TaskName                   FileName
--------------------------------------------------------------------------------
	task1                   task1.py
	task2                   invertedindex.py	
        task3                   UNIGRAM-TF.txt
			        UNIGRAM-DF.txt
			        BIGRAM-TF.txt
				BIGRAM-DF.txt
				TRIGRAM-TF.txt
				TRIGRAM-DF.txt
				Task_3_STOPLIST.pdf

--------------------------------------------------------------------------------
TF- Term Frequency
DF-Document Frequency	       
_____________________________________________________________________________________________________________________

Setup the file for execution

----- For task1.py-----
locate variables
1. source_path 
- provide the correct path where all the html files are located.
2. dest_path
- provide the correct path where the created files need to be stored.

----- For invertedindex.py-----
locate variable named path and provide the correct path where the cleaned html files are stored.
_____________________________________________________________________________________________________________________
To run the program 

-> Go to the folder where the file is located in command prompt
-> Steps to run programs
Step 1: change dir to the folder containing the python files in command prompt
Step 2: To run type >>>python <FileName>
		eg: >>>python invertedindex.py

			
_____________________________________________________________________________________________________________________
In order to successfully run this code ,we need following libraries

----task1.py----
1. from string import maketrans
2. import os
3. import re

----invertedindex.py----
1.import os
2.import operator
3.import re
_____________________________________________________________________________________________________________________
Design choices

-> Dict in python
	I have used dic to as the data structure as it allows flexibility to change values.

-> RE in python
	Allows us to manipulate the data and give the desired output
-> Path 
	Used absolute path name as the file location varies from system to system
-> Used individual helper functions for reuse of code

______________________________________________________________________________________________________________________
Sources of Information:

1. https://docs.python.org/2/library/functions.html
