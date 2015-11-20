'''
This script shows how to add persistence record storing of classes.
'''

import shelve
from h_step3ClassBehavior import Person
from h_step3ClassBehavior import Manager

bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 54, 40000, 'hardware')
tom = Manager('Tom Doe', 50, 50000)

'''
This is creating a shelve file that assigns class instances to individual keys
which is similar to a dictionary of class instances, but what would be the top
level dictionary is a shelve file.
'''
classShelve = './output/class-shelve'
db = shelve.open(classShelve)
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()

#the shelve can then be opened to read in the class instances
#if this opening was done in a separate script, the Person and Manager
#classes would not need to be reimported
db = shelve.open(classShelve)
for key in db:
    print(key, '=>\n ', db[key].name, db[key].pay)

print('\nAnd manually:')
bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())
