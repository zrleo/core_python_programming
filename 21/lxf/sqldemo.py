# -*- coding:utf-8 -*-

import MySQLdb

from DBUtils.PooledDB import PooledDB

pool = PooledDB(MySQLdb, 5, host='127.0.0.1', user='root', passwd='123456', db='test', port=3306)

conn = pool.connection()
cur = conn.cursor()
cur.execute('create table user (id varchar(20) primary key, name varchar(20))')
cur.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cur.rowcount

conn.commit()
conn.close()
