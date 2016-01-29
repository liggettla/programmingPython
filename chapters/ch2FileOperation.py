#this script deals with opening and reading files
entireFile = open('textfile.txt').read()
print(entireFile)
#just reads 10 bytes of the file into a string
entireFile = open('textfile.txt').read(10)
print(entireFile)
entireFile = open('textfile.txt').readlines()
#reds entire file into line strings list
print(entireFile)
firstLine = open('textfile.txt').readline()
print(firstLine)


