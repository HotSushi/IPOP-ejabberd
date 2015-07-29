# IPOP-ejabberd-loguploader
This should contain info on how to setup crontab

crontab -e
* * * * * python /home/adminuser/IPOP-ejabberd/log/script.py
change config.json with correct info
{
"admin_ip":"192.168.0.106",
"port":"8000",
"public_ip":"192.168.0.102",
"log_name":"ejabberd.log",
"log_location":"/var/log/ejabberd/ejabberd.log"
}

