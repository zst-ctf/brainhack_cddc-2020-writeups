# [OSINT-1] Funky Transfer Pact
Gate 4

## Challenge 

Being such a huge conglomerate, it can't be that they only have a tiny web server..


## Solution

Info we know so far:
- Company: UnduplicitousCorp
- Website: https://www.unduplicitouscorp.tech/

Get IP address of server

	$ nslookup www.unduplicitouscorp.tech
	Server:		127.0.0.53
	Address:	127.0.0.53#53

	Non-authoritative answer:
	Name:	www.unduplicitouscorp.tech
	Address: 13.76.37.209

Find open ports

	$ nmap 13.76.37.209
	Starting Nmap 7.80 ( https://nmap.org ) at 2020-07-04 10:29 +08
	Nmap scan report for 13.76.37.209
	Host is up (0.016s latency).
	Not shown: 996 filtered ports
	PORT    STATE  SERVICE
	20/tcp  closed ftp-data
	21/tcp  open   ftp
	80/tcp  open   http
	443/tcp open   https

	Nmap done: 1 IP address (1 host up) scanned in 4.78 seconds

We find an FTP server which accepts only anonymous users.

	$ ftp 13.76.37.209
	Connected to 13.76.37.209.
	220 Welcome to UnDuplicitousCorp FTP service.
	Name (13.76.37.209:zst): admin
	530 This FTP server is anonymous only.
	Login failed.
	
	$ ftp 13.76.37.209
	Connected to 13.76.37.209.
	220 Welcome to UnDuplicitousCorp FTP service.
	Name (13.76.37.209:zst): anonymous
	230 Login successful.
	Remote system type is UNIX.
	Using binary mode to transfer files.


Switch to passive mode

	ftp> passive
	Passive mode on.
	ftp> ls
	227 Entering Passive Mode (10,0,1,6,156,68).

https://ftptest.net/#result


## Flag

	?