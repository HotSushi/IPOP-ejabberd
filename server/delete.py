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
p = subprocess.Popen(["sudo", "-S", "./script.sh"],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
t = p.communicate(password+"\n") 

p = subprocess.Popen(["sudo", "-K"],stdin=subprocess.PIPE,stdout=subprocess.PIPE)

if t[0] == '':
    response = {'return_code':0,'msg':'node deleted'}
else:
    response = {'return_code':2,'msg':'Error occurred in ejabberd server (Did you enter the correct sudo password?)'}

print(json.JSONEncoder().encode(response))
