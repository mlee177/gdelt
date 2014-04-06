#!/bin/env python

import pymysql
import datetime
import json
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
  passwd='password',db='gdelt')

cur = conn.cursor()

def getBetweenDates(start,end):
  """ start and end are dates in the format %Y-%m-d """
  startdate = datetime.datetime.strptime(start, "%Y-%m-%d") #2001-03-04
  enddate = datetime.datetime.strptime(end,"%Y-%m-%d")
  
  statement = "SELECT id FROM gdelt WHERE conflict_date > '{start}' AND\
 conflict_date < '{end}'".format(start=startdate, end=enddate)
  print(statement) 
  cur.execute(statement)
  return cur.fetchall() 
  #for r in cur.fetchall():
  #  print(r[0])

def getBetweenGoldstein(mings,maxgs):
  statement = "SELECT id,goldstein FROM gdelt WHERE goldstein > {mng}\
  AND goldstein < {mxg};".format(mng=mings,mxg=maxgs)
  print(statement)
  cur.execute(statement)
  return cur.fetchall()
  #for r in cur.fetchall():
  #  print(r)


def getEventCodeDescription(eventcode):
  statement = "SELECT id,description FROM eventcode WHERE id='{}'".format(eventcode)
  print(statement)
  cur.execute(statement)
  r = cur.fetchone()
  return r
  #print(r)

def getAllBetweenTwoCountries(c1,c2):
  """ c1 and c2 are three letter country codes """
  statement = "SELECT id, source_country, target_country from gdelt where (source_country='{0}' AND target_country='{1}') OR (source_country='{1}' AND target_country='{0}');".format(c1.upper(),c2.upper())
  print(statement)
  #print(statement)
  cur.execute(statement)
  return cur.fetchall()
  #for r in cur.fetchall():
  #  print(r)

def sumGoldstein(c1,c2):
  """ """
  statement = "SELECT SUM(goldstein) from gdelt where\
   (source_country='{0}' AND target_country='{1}') OR\
   (source_country='{1}' AND target_country='{0}');".format(
   c1.upper(),c2.upper())
  
  print(statement)
   
  cur.execute(statement)
  return cur.fetchone()

def sumEvents(country,event,start,end):
  startdate = datetime.datetime.strptime(start, "%Y-%m-%d") #2001-03-04
  enddate = datetime.datetime.strptime(end,"%Y-%m-%d")

  statement = "SELECT COUNT(cameo_code) from gdelt where\
  target_country='{c}' AND cameo_code='{e}' WHERE conflict_date > '{sd}'\
  AND conflict_date < '{ed}';".format(c=country,e=event,sd=startdate,
  ed=enddate);

  print(statement)

  cur.execute(statement)
  return cur.fetchone()

def convertJSON(obj):
  json_string = json.dumps(dict(obj))
  return json_string

