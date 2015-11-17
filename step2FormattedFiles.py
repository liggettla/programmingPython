#this script focuses on outputting data structures to file

#this initializes data to be stored in files, pickles, and shelves
bob = {'name':'Bob Smith', 'age':42, 'pay':30000, 'job':'dev'}
sue = {'name':'Sue Jones', 'age':45, 'pay':40000, 'job':'hdw'}
tom = {'name':'Tom',       'age':50, 'pay':0,     'job':None}

#setup database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':
    for key in db:
        print(key, '=>\n ', db[key])

'''
The following portion of the script saves in-memory database info to a file
with some custom formatting. 'endrec.', 'enddb.', and '=>' must not be used
in the data. db is a dictionary of dictionaries
This is also bad code because it rus strings as code.
Could also use: dbfile.write(key + '\n') instead of print(key, file=dbfile);
'''

dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def storeDbase(db, dbfilename=dbfilename):
    "formatted dump of database to flat file"
    dbfile = open(dbfilename, 'w')

    for key in db:
        print(key, file=dbfile)
        #items() turns keys and values into lists
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()

def loadDbase(dbfilename=dbfilename):
    "parse data to reconstruct database from output file"
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db

storeDbase(db, dbfilename)

'''
if __name__ == '__main__':
    from initdata import db
    storeDbase(db)
    '''
