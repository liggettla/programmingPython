'''
This code demonstrates how to output pickle files
One advantage of this is that the entire database will not have to be written
to file again after modifying any of the data.
Another advantage is that random separators do not need to be created that may
complicate the output.
Python's pickle module overcomes these problems by translating an in-memory python object like a dictionary into a string of bytes that can be written to any file-like object, and theis can be reconstructed back into the original in-memory data structure from file.
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

import pickle
dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
