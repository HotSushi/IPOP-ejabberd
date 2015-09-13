import time 
import os
import json
import urllib2
import urllib

DIR = os.path.dirname(os.path.realpath(__file__))
global LOG_LOC,IP,ADMIN_IP,PORT,LOG_NAME

def read():
    try:
        lu = open(DIR+'/last_updated','r')
    except:
        lu = open(DIR+'/last_updated','w')
        lu.write('2015-07-11 11:23:12')
        lu.close()
        return read()
    tm = strtotime(lu.read())
    lu.close()
    return tm

def write(ct):
    lu = open(DIR+'/last_updated','w')
    lu.write(ct)
    lu.close()

def strtotime(st):
    return time.strptime(st, "%Y-%m-%d %H:%M:%S") 

def process():
    write_buffer = ''    
    with open(LOG_LOC,'r') as fi:
        lines = fi.readlines()
        last_time = read()
        i = 0
        while i< len(lines):
            line = lines[i]
            #=INFO REPORT==== 2015-07-11 14:30:35 ===
            if "INFO REPORT" in line:
                listt = line.split('=')
                listt = filter(None,listt)
                current_time =  listt[-2].strip()
                #read next line
                i+=1
                line = lines[i]
                if strtotime(current_time) > last_time:
                    listt = line.split(' : ')
                    data = listt[1:]
                    write_buffer = current_time+' > '+data[0] +'\n'+ write_buffer
            i += 1
        if write_buffer:
            try:
                send(write_buffer)
            except ValueError:
                return
        write(current_time)

def generate_URL():
    baseurl = 'http://%s:%s/IPOP/default/log'
    url = baseurl%(ADMIN_IP,PORT)
    return url

def send(data):
    values = {'type':'set','node':IP,'name':LOG_NAME,'log':data}
    url_data = urllib.urlencode(values)
    try:        
        response = urllib2.urlopen(generate_URL()+'?'+url_data)
    except urllib2.URLError, e:
        open(DIR+'/error','w').write(str(e))
        raise ValueError(str(e))
    return response.read()

if __name__ == "__main__":
    with open(DIR+'/config.json','r') as config_file:
        data = json.load(config_file)
        LOG_LOC = data['log_location']
        LOG_NAME = data['log_name']
        IP = data['self_ip']
        ADMIN_IP = data['admin_ip']
        PORT = data['port']
        config_file.close()
    process()



