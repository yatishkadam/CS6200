from string import maketrans
import os
import re


source_path = 'C:\Users\yatish\Desktop\IR\hw3\\textfiles'
dest_path= 'C:\Users\yatish\Desktop\IR\hw3\parsedtextfiles'
file_namelist = []
dirs = os.listdir(source_path)
intab = "!\"#$%&\'()*+,./:;<=>?@[\]^_`{|}~"
outtab = "                               "
trantab = maketrans(intab, outtab)
cleanr = re.compile('<.*?>')

def isalpnum(input):
    return any(char.isdigit() for char in input)

def change_to_string(inputstring):
    length=len(inputstring)
    flag = True
    s = ""
    for i in range(0, length):
        if inputstring[i].isalpha() or inputstring[i] == '-':
            flag = False
            s += str(inputstring[i])
        elif inputstring[i].isdigit():
            s += str(inputstring[i])
            if any(char.isdigit() for char in inputstring[(i + 1):]):
                flag = True
            else:
                flag = False
        elif flag:
            s += str(inputstring[i])
        else:
            s += str(' ')
    return s

def corpus(path):
    for file in dirs:
        f = open(path + '\\' + file, 'r+')
        string = f.read()
        string_lower = string.lower()
        new_string = string_lower.split()
        string = " ".join(new_string)
        s=''
        for char in file:
            if char.isalpha() or char.isdigit():
                s += char
        pat = re.search(r'txt', s)
        name = s[:pat.start()]
        i=0
        if name not in file_namelist:
            file_namelist.append(name)
        else:
            i += 1
            name += str(i)
            file_namelist.append(name)
        cleantext = re.sub(cleanr, '', str(string))
        latest_string = ''
        latest_string+= name+'\n'
        new_text = cleantext.split(" ")
        for i in new_text:
            if not isalpnum(i):
                latest_string += i.translate(trantab) + " "
            else:
                latest_string += change_to_string(i) + " "
        write_to_file(name,latest_string)
        f.close()

def write_to_file(name,output_string):
    name += ".txt"
    f = open(dest_path + '\\' + name, 'w')
    f.write(output_string)
    f.close()

# Main function call
corpus(source_path)