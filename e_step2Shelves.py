'''
Pickling is oftentimes sufficient to store data, especially if there is no file number limit, but if storing as an entire database becomes necessary, then shelves provide this option
Shelves automatically pickle objects to and from a keyed=access filesystem.
Because they are key-based there is no need to manually manage one file per
record.
'''

import shelve

bob = {'name':'Bob Smith', 'age':42, 'pay':30000, 'job':'dev'}
sue = {'name':'Sue Jones', 'age':45, 'pay':40000, 'job':'hdw'}
dbTemp = {}
dbTemp['bob'] = bob
dbTemp['sue'] = sue
print('This is the structure of the shelve')
print(dbTemp)

shelveOut = './output/people-shelve'
db = shelve.open(shelveOut)
db['bob'] = bob
db['sue'] = sue
db.close()

db = shelve.open(shelveOut)
print('\nThis is accessing a record from the shelve')
print(db['bob'])
db.close()

#shelves are edited just like dictionaries
print('\nThis is editing a single record')
db = shelve.open(shelveOut)
sue = db['sue']
sue['pay'] *= 1.50
db['sue'] = sue
print(db['sue'])
#The following does not work with shelves
#data must be read into memory, modified there and then written back to shelve
#db['sue']['pay'] = 90000
print(db['sue']['pay'])
db.close()
