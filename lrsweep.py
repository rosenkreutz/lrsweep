#!/usr/bin/python3.2
#nmap ping-sweep output cleaning tool
#written by pseudophed (like a champ)
# lrsweep.py
# o7 bitches #

import argparse, re, sys, errno, os

def run():
	
	try:
		scanFile = open(args.inputFile, 'r')
	except IOError as err:
		print('I/O Error')
		print('Error(' + format(err.errno) + '): ' + format(err.strerror))
		sys.exit(1)
	

	if (args.outputFile):
	
		try:
			writeFile = open(results.outputFile, 'w')
	    except IOError as err:
			print('I/O Error')
			print('Error(' + format(err.errno) + '): ' + format(err.strerror))
			sys.exit(1)
	
		for line in scanFile:
			if (line.find('host down') < 0 and line.find('latency') < 0 and line.find('packet') < 0):
				ip_candidates = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
			
			if (ip_candidates):
				writeFile.write(ip_candidates[0])
				writeFile.write('\n')
				writeFile.close()
			
			print ('File Written. Review results in', args.outputFile)
			sys.exit(0)
			
	else:
    
		for line in scanFile:
			if (line.find('host down') < 0 and line.find('latency') < 0 and line.find('packet') < 0):
				ip_candidates = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
			
			if ip_candidates:
				print (ip_candidates[0], end='\n')
	
		scanFile.close()
		sys.exit(0)

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Cleans nmap output files', prog='lrsweep')
	parser.add_argument('-iF', action='store', dest='inputFile', help='nmap ping sweep output file', required=True)
	parser.add_argument('-oF', action='store', dest='outputFile', help='Output file for cleaned list')
	parser.add_argument('--version', action='version', version='%(prog)s 1.1')
	
	args = parser.parse_args()

	run()