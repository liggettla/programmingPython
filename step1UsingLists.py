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

#the advantage of lamdab can be seen when used with map
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

print('Using the generator expression; sum')
print(sum(person[2] for person in people))

