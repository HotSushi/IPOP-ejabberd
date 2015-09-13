# IPOP-ejabberd log uploader
The python script `script.py` uploads ejabberd log to [IPOP-server](https://github.com/HotSushi/IPOP-server)

## How to set it up?

### First modify `config.json`
```
{
"admin_ip":"192.168.0.106",     # IP of IPOP-server
"port":"8000",                  # port no of IPOP-server
"self_ip":"192.168.0.102",      # self public IP
"log_name":"ejabberd.log",      # log name to be saved on the server
"log_location":"/var/log/ejabberd/ejabberd.log"     # location of ejabberd log file
}
```

### Then schedule a crontask
run `crontab -e`, to open it with your favorite editor.

append with the following, with correct location of the script
```
* * * * * python /home/adminuser/IPOP-ejabberd/log/script.py
```

### Check log file on IPOP-server
On [IPOP-server](https://github.com/HotSushi/IPOP-server), go to `Edit GVPN` tab, click on ejabberd node of the VPN.  And check if `ejabberd.log` is present.