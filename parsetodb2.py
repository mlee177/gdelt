#!/bin/env python
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='password',db='gdelt')

cur = conn.cursor()

f = open("CAMEO.eventcodes.txt",'r')
f.readline() #Skip first line

for line in f.readlines():
  fields = line.strip().split('\t')
  
  statement = "INSERT INTO gdelt.eventcode (id,description) VALUES\
  ('{id}','{desc}');".format(id=fields[0],desc=fields[1])
  print(statement)

  cur.execute(statement)

conn.commit()
conn.close()

