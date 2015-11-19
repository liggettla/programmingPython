'''
One advantage that classes provide over the use of dictionaries to store and process
data is that classes naturally associate reocrd data with processing logic, and
allows the logic to be changed once without redundancy.
'''
class Person:
    #here pay=0 and job=None are used so that they will have default values in case
    #no pay or job title are passed
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

'''
the following line is a check that this is the main script being run, when this
script is directly run in the terminal the special __name__ variable is set to
__main__ but if this file is being imported from another module __name__ will be set
to that modules name. This prevents the following code from executing unless this
script is the main script that is run.
'''
if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    print(bob.name, sue.pay)

    print(bob.name.split()[-1])
    sue.pay *= 1.10
    print(sue.pay)
