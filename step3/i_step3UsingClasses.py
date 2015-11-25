'''
This script shows how classes can be used to create a database and modify elements
within it.
'''

from h_step3ClassBehavior import Person
from h_step3ClassBehavior import Manager

bob = Person(name='Bob Smith', age=42, pay=10000)
sue = Person(name='Sue Jones', age=45, pay=20000)
tom = Manager(name='Tom Doe', age=55, pay=100000)

db = [bob, sue, tom]

for obj in db:
    obj.giveRaise(.10)

for obj in db:
    print(obj.lastName(), '=>', obj.pay)
