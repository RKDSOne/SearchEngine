#!/usr/bin/env python
import cgi
import cgitb
import sys
import json

print ("Content-Type: application/json")
field_store = cgi.FieldStorage()

print 
print ('''<script>alert("aler")</script>''')
print ("\n\n")

ans = {}
ans['success'] = True
ans['message'] = "Query Successful"
new_array = {}
for i in field_store.keys():
    new_array[i] = field_store.getvalue(i)
ans['data'] = new_array
target = open("ans_log.txt", 'a')
target.write(json.dumps(ans,indent=1))
target.write("\n")
target.close()