#using import command for system specific parameters
import sys

#defined a function called  l33t
def l33t(line):
	letmsg = line
	letwords = "oOaAeEiI"
	global count
	for letter in line:
	count += 1
	if letter in letwords:
		letmsg = letmsg.replace('o',str(0))
		letmsg = letmsg.replace('O',str(0))
		letmsg = letmsg.replace('a',str(4))
		letmsg = letmsg.replace('A',str(4))
		letmsg = letmsg.replace('e',str(3))
		letmsg = letmsg.replace('E',str(3))
		letmsg = letmsg.replace('i',str(1))
		letmsg = letmsg.replace('I',str(1))
		return letmsg

def fun(read,wr):
	global linecount
	with open(read) as F1:
		if wr:
			myfile = wr
		else:
			myfile = "test.txt"
