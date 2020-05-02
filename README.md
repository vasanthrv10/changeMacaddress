# changeMacaddress
Simple python script for automate the process of macaddress modification.....!


To know the value of arguments:
	cmd:
		$ python changemac.py --h
				(or)
		$ python changemac.py --help


To set a custom mac address:-
	syntax:
		$ python changemac.py -i [interface] -set [mac-address]
	eg:
		$ python changemac.py -i eth0 -set a6:00:8d:54:cf:e6


To set a random mac address:-
	syntax:
		$ python changemac.py -i [interface] -random ok
	eg:
		$ python changemac.py -i eth0 -random ok


Reset to the original mac address:-
	syntax:
		$ python changemac.py -i [interface] -reset
	eg:
		$ python changemac.py -i eth0 -reset



		NOTE :
			-> if you use ethernet give 'eth0' for '-i' argument....
			-> if you use wifi give 'wlan0' for '-i' argument....
