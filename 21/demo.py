# -*- coding:utf-8 -*-

import os
from random import randrange as rrange


COLSIZ = 10
RDBMSs = {'s': 'sqlite', 'm': 'mysql', 'g': 'gadfly'}
DB_EXC = None


def setup():
    return RDBMSs[raw_input(
        '''
        choose a database system:
        (M)ysql
        (S)qlite
        (G)adfly
        Enter choice:
        ''')].strip().lower()[0]


def connect(db, dbname):
    global DB_EXC
    dbdir = '%s_%s' % (db, dbname)
    if db == 'sqlite':
        try:
            import sqlite3
        except ImportError as e:
            try:
                from pysqlite2 import dbapi2 as sqlite3
            except ImportError, e:
                return None
            DB_EXC = sqlite3
            if not os.path.isdir(dbdir):
                os.mkdir(dbdir)
            cxn = sqlite3.connect(os.path.join(dbdir, dbname))
    elif db == 'mysql':
        try:
            import MySQLdb
            import _mysql_exceptions
        except ImportError, e:
            return None
        try:
            cxn = MySQLdb.connect(db= dbname)
        except DB_EXC.OperationalError, e:
            cxn = MySQLdb.connect('root')
        try:
            cxn.query('DROP DATABASE %s' % dbname)
        except _mysql_exceptions.OperationalError, e:
            pass
        cxn.query('create database %s' % dbname)
        cxn.query("grant all on %s. * to ''@'localhost'" % dbname)
        cxn.commit()
        cxn.close()
        cxn = MySQLdb.connect(db=dbname)


def create(cur):
    try:
        cur.execute(''' create table users(login VARCHAR (8),uid INTEGER ,prid INTEGER )''')
    except DB_EXC.OperationalError, e:
        drop(cur)
        create(cur)
drop = lambda cur: cur.execute('DROP TABLE users')

NAMES = (
    ('arron', 8312), ('angela', 7603), ('dave', 7306),
    ('adah', 7902), ('ekahd', 7911), ('dagdsad', 7410),
    ('arron', 8312), ('angela', 7603), ('dave', 7306),
    ('adahdas', 7902), ('ekadsahd', 7911), ('dagdxcsad', 7410),
    ('adacxzh', 7902), ('ekashd', 7911), ('dagdsad', 7410),
    ('arrczon', 8312), ('angedla', 7603), ('dasave', 7306),
    ('arrczon', 8312), ('angecla', 7603), ('davaae', 7306),
    ('davce', 7306),
)


def randNmae():
    pick = list(NAMES)
    while len(pick) > 0:
        yield pick.pop(rrange(len(pick)))


def insert(cur, db):
    if db == 'sqlite':
        cur.executemany('INSERT INTO USERS VALUES(?,?,?)', [(who, uid, rrange(1, 5)) for who, uid, in randNmae()])
    elif db == 'mysql':
        cur.executemany('INSERT INTO USERS VALUES(%s,%s,%s)', [(who, uid, rrange(1, 5)) for who, uid, in randNmae()])

getRC = lambda cur: (hasattr(cur, 'rowcount') and [cur.rowcount] or [-1])[0]


def update(cur):
    fr = rrange(1, 5)
    to = rrange(1, 5)
    cur.execute('update users set prid = %d where prid = %d'(to, fr))
    return fr, to, getRC(cur)


def delete(cur):
    rm = rrange(1,5)
    cur.execute('delete from users where prid=%d' % rm)
    return rm, getRC(cur)


def dbDump(cur):
    cur.execute('select * from users')
    print '\n%s%s%s' % ('login'.ljust(COLSIZ),
                        'USERID'.ljust(COLSIZ), 'PROJ#'.ljust(COLSIZ))
    for data in cur.fetchall():
        print '%s%s%s' % tuple ([str(s).title.ljust(COLSIZ) for s in data])


def main():
    db = setup()
    print '*** Connecting to %r database' % db,

    cxn = connect(db, 'test')
    if not cxn:
        print 'ERROR: %r not supported, exitting' %db,
        return
    cur = cxn.curses()

    print '\n*** Creating users table',\
    create(cxn)
    print '\n*** Inserting names into tables',\
    insert(cur, db)
    dbDump(cur)
    print '\n*** Randomly choosing group',
    rm, num = delete(cur)
    print '(%d) to delete' % rm
    print '\t(%d users removed)' % num
    dbDump(cur)
    print '\n*** Randomly moving folks',
    fr, to, num = update(cur)
    print 'from one group (%d) to another (%d) ' %(fr, to)
    print '\t(%d users moved)'%num
    dbDump(cur)
    print '\n*** Dropping users table'
    drop(cur)
    cur.close()
    cxn.commite()
    cxn.close()

if __name__ == '__main__':
    main()
