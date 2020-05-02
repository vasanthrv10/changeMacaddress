
#!/usrbin/env python

from distutils.spawn import find_executable
from argparse import ArgumentParser
from subprocess import call
from random import choice


#function for generate random mac address.....
def randommac():
	alphanumeric = '0123456789abcdef'
	return ':'.join((choice(alphanumeric)+choice(alphanumeric)) for i in range(6))


#code for receive arguments.... 

parser = ArgumentParser(description="Demo usage of this program:")
parser.add_argument('-i', dest='interface', type=str, required=True, help='specify network interface')
parser.add_argument('-reset', dest='rst', help='to setback the original mac address')
parser.add_argument('-set', dest='new_mac', type=str, help='specify new macaddress')
parser.add_argument('-random', dest='rdm', help='to set random macaddress')
arguments = parser.parse_args()


#code for process random option....
if arguments.rdm=='ok':
	randmac = randommac()
	call(['ifconfig',arguments.interface,'down'])
	call(['ifconfig',arguments.interface,'hw','ether',randmac])
	call(['ifconfig',arguments.interface,'up'])


#code for process reset option
if arguments.rst=='ok':
	if find_executable('macchanger')==None:
		call(['sudo','apt','install','macchanger'])
	call(['macchanger','-p',arguments.interface])


#code for process of assign user define mac....
if arguments.new_mac!=None:
	try:
		call(['ifconfig',arguments.interface,'down'])
		call(['ifconfig',arguments.interface,'hw','ether',arguments.new_mac])
	except:
		call(['ifconfig',arguments.interface,'up'])
		print("Please enter mac in correct format...!")
	finally:
		call(['ifconfig',arguments.interface,'up'])

call(['ifconfig',arguments.interface])
