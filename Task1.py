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

	with open(myfile,"w") as F2:
		for line in F1:
			linecount =+ 1
			new =l33t(line)
			F2.write(new)
	return myfile

def report(opr):
	print(f"Pages Copied: {linecount/25}")
	print(f"Lines Copied: {linecount}")
	print(f"Words Copied: {count}")
	print(f"Pages Copied: {linecount/25}")
	alpha = 0
	num = 0
	with open(opr,'r') as docs:
		for line in docs.readline():
			for letter in line.lower():
				if letter.isaplha():
					alpha += 1
				if letter.is():
					num += 1
	print(f"Alphanumeric Characters:{alpha}")
	print(f"Numeric Characters : {num}")

	try:
		count = 0
		linecount = 0
		print("This program lets you copy content of a file to another")
		fin = input("enter the file name:" \n)
		fout = output("Enter the output filename:" \n)
		dest = fun(fin,fout)
		print(f"The file has bene copied to: {dest}")
		report(dest)
 
	except:
		print("Exception")
		exit()

