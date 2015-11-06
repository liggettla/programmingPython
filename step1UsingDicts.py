#Uses python 3.x
import pprint

#using dictionaries is typically more convenient than using field labels
print('\nUsing a simple dictionary')
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
print(bob['name'], sue['pay'])
print(bob['name'].split()[-1]) #print last name

#because dicts are so useful there are even faster ways of creating them
#the following can be used so long as all the keys are strings
print('\nOther ways of creating dictionaries')
bob = dict(name = 'Bob Smith', age = 42, pay = 30000, job = 'dev')
sue = dict(name = 'Sue Jones', age = 45, pay = 40000, job = 'hdw')
print(bob)

#dictionares can be created one field at a time
print('\nDictionaries can be also created one field at a time')
sue = {}
sue['name'] = 'Sue Jones'
sue['age'] = 45
sue['pay'] = 40000
sue['job'] = 'hdw'
print(sue)

#dictionaries can also be made by zipping together name and
#value lists
print('\nZipping together names and values')
names = ['name', 'age', 'pay', 'job']
values = ['Sue Jones', 45, 40000, 'hdw']
print(list(zip(names, values)))
print(dict(zip(names, values)))

#empty dictionaries can also be initialized in the same way the same
#value can be set for every initialized key
print('\nEmpty dictionary creation')
fields = ('name', 'age', 'job', 'pay')
record = dict.fromkeys(fields, '?')
record2 = dict.fromkeys(fields, )
print(record)
print(record2)

#lists of dictionaries
print('\nLists of dictionaries')
people = [bob, sue]
for person in people:
    print(person['name'], person['pay'], sep=', ') #separation char, only works in python 3.x

for person in people:
    if person['name'] == 'Sue Jones':
        print(person['pay'])

#iteration tools can be used here to look through positions
print('\nIterating through dictionaries')
names = [person['name'] for person in people]
print(names)

print(list(map((lambda x: x['name']), people))) #collect names

print(sum(person['pay'] for person in people)) #sum all pay

#list comprehensions can approach the utility of SQL queries
print([rec['name'] for rec in people if rec['age'] >= 45])
print([(rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people])

G = (rec['name'] for rec in people if rec['age'] >= 45)
print(next(G))

G = ((rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people)
print(next(G)) #does the same as the following line
print(G.__next__())

#because dictionaries are objects, they can be accesed and updated
print('\nDictionaries can be updated')
for person in people:
    print(person['name'].split()[-1]) #print last name
    person['pay'] *= 1.10
    print(person['pay'])

#nested structures
print('\nOne of the advantages of scripting languages is that they can build nested structures and later reclaim the memory after this has been done')
bob2 = {'name':{'first':'Bob','last':'Smith'}, 'age': 42, 'job': ['software', 'writing'], 'pay': (40000, 50000)}
#now simply index twice to get a value that is two levels deep
print(bob2['name']) #full name
print(bob2['name']['last']) #last name
bob2['pay'][1] #upper pay

for job in bob2['job']: print(job)
bob2['job'][-1] #bob's last job
bob2['job'].append('janitor') #time for a new job
for job in bob2['job']: print(job)

#dicts of dicts
print('\nDictionaries can also be made out of dictionaries')
bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
print(sue)
db = {}
db['bob'] = bob
db['sue'] = sue
print(db)
print(db['bob']['name'])
print(db['sue']['pay'])
db['sue']['pay'] = 50000 #change value
print(db['sue']['pay'])
pprint.pprint(db) #pretty print clearly displays nested data structures

print('\nIterating through nested dictionaries')
for key in db:
    print(key, 'salary =>', db[key]['pay'])

#visiting all records by key
for key in db:
   print(db[key]['name'].split()[-1])
   db[key]['pay'] *= 1.10

for record in db.values(): print(record['pay'])

#adding records with new keys
print('\nAdding records with new keys')
db['sue']['pay'] = 50000 #change value
pprint.pprint(db)
db['tom'] = dict(name='Tom', age=50, job=None, pay=0)
print('\n')
pprint.pprint(db)
print('length of db:', len(db))
