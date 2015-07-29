#!/usr/bin/python
import subprocess
import cgi
import cgitb; cgitb.enable()
import json 


print "Content-type:application/json\r\n\r\n"

arg = cgi.FieldStorage()
text = arg.getvalue('cmd')
password = arg.getvalue('pw')
with open('script.sh','w') as sc:
    sc.write(text)

#echo adminuser | sudo -S ls
#p= subprocess.Popen('echo adminuse | sudo -S ./script.sh',shell=True,stdout=subprocess.PIPE)

#run script with sudo right
p = subprocess.Popen(["sudo", "-S", "./script.sh"],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
t = p.communicate(password+"\n") 
#revoke sudo rights
p = subprocess.Popen(["sudo", "-K"],stdin=subprocess.PIPE,stdout=subprocess.PIPE)

if 'Can\'t register' in t[0]:
    response = {'return_code':2,'msg':'instructions sent are incorrect'}
elif 'successfully registered' in t[0]:
    response = {'return_code':0,'msg':'success'}
elif 'already registered' in t[0]:
    response = {'return_code':0,'msg':'success'}
else:
    response = {'return_code':2,'msg':'reasons unknown, pls file a bug, error occurred in ejabberd server'}

print(json.JSONEncoder().encode(response))
