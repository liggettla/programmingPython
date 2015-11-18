'''
Pickling is oftentimes sufficient to store data, especially if there is no file number limit, but if storing as an entire database becomes necessary, then shelves provide this option
Shelves automatically pickle objects to and from a keyed=access filesystem.
Because they are key-based there is no need to manually manage one file per
record.
'''

import shelve

bob = {'name':'Bob Smith', 'age':42, 'pay':30000, 'job':'dev'}
sue = {'name':'Sue Jones', 'age':45, 'pay':40000, 'job':'hdw'}

shelveOut = './output/people-shelve'
db = shelve.open(shelveOut)
db['bob'] = bob
db['sue'] = sue
db.close()
