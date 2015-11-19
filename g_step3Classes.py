from f_step3Classes import Person

bob = Person('Bob Smith', 42)
sue = Person('Sue Jones', 45, 40000)
#create a database of classes
people = [bob, sue]
for person in people:
    print(person.name, person.pay)

x = [(person.name, person.pay) for person in people]
print(x)

#SQL-ish queries can be made for classes
print('\nSQL-ish queries can be made for classes')
x = [(rec.age ** 2 if rec.age >= 45 else rec.age) for rec in people]
print(x)
