'''
This code demonstrates how to output pickle files
One advantage of this is that the entire database will not have to be written
to file again after modifying any of the data.
Another advantage is that random separators do not need to be created that may
complicate the output.
Python's pickle module overcomes these problems by translating an in-memory python object like a dictionary into a string of bytes that can be written to any file-like object, and theis can be reconstructed back into the original in-memory data structure from file.
'''

import pickle
import pprint
from glob import glob
'''
glob finds all pathnames matching a specific pattern as in the following:
glob.glob('*.gif')
output: ['1.gif', 'card.gif']
'''

#this initializes data to be stored in files, pickles, and shelves
bob = {'name':'Bob Smith', 'age':42, 'pay':30000, 'job':'dev'}
sue = {'name':'Sue Jones', 'age':45, 'pay':40000, 'job':'hdw'}
tom = {'name':'Tom',       'age':50, 'pay':0,     'job':None}

#setup database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

#this dumps the dictionary structure to a pickle file
outputFile = './output/people-pickle'
dbfile = open(outputFile, 'wb') #b is for binary output
pickle.dump(db, dbfile)
dbfile.close()

dbfile = open(outputFile, 'rb')
db = pickle.load(dbfile)
pprint.pprint(db)
print('\nManual record calling:')
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])
dbfile.close()

#Updating a pickle file can be similar to editing a manually formatted file
#this is as inefficient as outputting to a manually formatted file each time
#new output is required
dbfile = open(outputFile,'wb')
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
pickle.dump(db, dbfile)
dbfile.close()

print('\nEdited Pickle File')
dbfile = open(outputFile, 'rb')
db = pickle.load(dbfile)
pprint.pprint(db)

#one way to overcome the inefficiency of rewriting the entire database to a pickle
#file is by writing each record in a separate file

#the following for-loop is saying print(key) and print(bob) because it is not iterating
#over the bob dictionary it just prints bob rather than iterating through the bob
#dictionary and printing keys as the following code would:
#for key in bob:
#   print key
for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
    recOutput = './output/' + key + '.pkl'
    recfile = open(recOutput, 'wb')
    pickle.dump(record, recfile)
    recfile.close()

#the following code dumps the entire database
for filename in glob('*.pkl')
#pg 64
