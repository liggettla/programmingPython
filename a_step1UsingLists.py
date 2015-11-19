#This script uses python 3

bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']

print(bob[0]) #name
print(sue[2]) #salary

bob[0].split()[-1] #get last name

sue[2] * 1.25 #give sue a 25% raise
print(sue)

#using a database list
print('\nUsing a database list:')
people = [bob, sue]
for person in people:
    print(person)

people[1][0] #sue's name

for person in people:
    print(person[0].split()[-1]) #print last names
    person[2] *= 1.20 #give each person a raise

for person in people:
    print(person[2]) #print new salaries

pays = [person[2] for person in people]
print(pays)

#lamda allows for the creation of a function that can then be used
#it is first passed the variables, then the function
print('\nUsing lambda function')
f = lambda x, y: x + y
print(f(1,1))

#the advantage of lambda can be seen when used with map
#map takes two args, first is the name of the function, the second is a sequence
#r = map(func, seq)
#map then applies the function to all elements of the sequence
def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)

temp = (36.5, 37, 37.5,39)

F = map(fahrenheit, temp)
C = map(celsius, F)
print('\nUsing the map() function')
print(F)
print(C)

print('\nUsing map() with lamdba')
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
print Fahrenheit
print C

print('\nUsing the map generator from 3.x')
pays = map((lambda x: x[2]), people)
print(list(pays))

print('\nUsing the generator expression, sum')
print(sum(person[2] for person in people))

#append and extend can add records to a list
print('\nAppend new record')
people.append(['Tom', 50, 0, None])
print(len(people))
print(people[-1][0])

#field labels allows a list index to be associated with a name
print('\nField labels can be used to reference list positions')
NAME, AGE, PAY = range(3)
print(NAME, AGE, PAY)
bob = ['Bob Smith', 42, 10000]
print(bob[NAME])
print(PAY, bob[PAY])

#a lists of lists would allow for field names to be directly associated
#with values in a list
print('\nField labels as embedded lists')
bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]
#while this method does allow a given field label to forever be associated with
#a particular value, calling still must be done by indexing by position
for person in people:
    print(person[0][1], person[2][1]) #prints name and pay
for person in people:
    print(person[0][1].split()[-2]) #get first names
    person[2][1] *= 1.10 #give 10% raise
for person in people:
    print(person[2])

#all the above has really done is add an extra level of positional indexing
#to do better the field names could be inspected within a loop
#using tuple assignment to unpack name/value pairs
print('\nUsing tuple assignment to search for field names')
for person in people:
    for (name, value) in person:
        if name == 'name': print(value) #find a specific field

#better is coding a fetcher function to automatically search
print('\nUsing automatic fetching function')
def field(record, label):
    for (fname, fvalue) in record:
        if fname == label:
            return fvalue

print(field(bob, 'name'))
print(field(sue, 'pay'))

for rec in people:
    print(field(rec, 'age')) #print all ages

#in the end it is more convenient to just use dictionaries when possible
