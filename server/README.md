# IPOP-ejabberd server
This server needs to be running for [IPOP-server](https://github.com/HotSushi/IPOP-server) to have functionality of `batch GVPN`.

## How it works?
This server receives `ejabberdctl` commands and `sudo password`(required to run those commands) from IPOP-server. It runs those commands and gives back the response to IPOP-server. Right now, it supports functionality of registering and deleting multiple nodes. This server runs on port `7000`.

## How to setup?
### First
```
chmod +x server.py
chmod +x script.sh
chmod +x delete.py
chmod +x create.py
```
### Then
```
./server.py
```