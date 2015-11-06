#Uses python 3.x

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
