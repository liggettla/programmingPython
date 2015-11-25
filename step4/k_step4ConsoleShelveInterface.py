'''
This allows for interactive queries allowing a user in the console to get
data from a shelve.
'''

import shelve

classShelve = './output/class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')
#this gets the longest length of any of the fieldnames by creating a list
#and finding the highest number in that list
maxfield = max(len(f) for f in fieldnames)
db = shelve.open(classShelve)

while True:
    key = input('\nKey? => ')
    if not key: break
    try:
        record = db[key]
    except:
        print('No such key "%s"!' % key)
    else:
        for field in fieldnames:
            #now the output is justified to the longest fieldname so they
            #all line up
            print(field.ljust(maxfield), '=>', getattr(record, field))
            #the following shifts everything over by 10 chars
            #print(field.ljust(10), '=>', getattr(record, field))
