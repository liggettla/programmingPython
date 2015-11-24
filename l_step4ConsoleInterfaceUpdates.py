#This script not only allows for console interaction to read back info to the
#user, but it also allows updates to the database

import shelve
from h_step3ClassBehavior import Person

classShelve = './output/class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')

db = shelve.open(classShelve)
while True:
    key = input('\nKey? => ')
    if not key: break #In case input is just Enter

    if key in db: #steps through list of keys
        record = db[key]
    else:
        record = Person(name='?', age='?')

    for field in fieldnames:
        currval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))
        if newtext:
            #this is equivalent to record.field = eval(newtext)
            #which seems more common
            #ie bob.age = 95
            setattr(record, field, eval(newtext))
            #eval evaluates an expression as python syntax
            #like the following:
            #print(eval('x + 1'))

    db[key] = record
db.close()
