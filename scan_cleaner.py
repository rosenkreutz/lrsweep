#!/usr/bin/python3.2
#nmap ping-sweep output cleaning tool
#written by pseudophed (like a champ)
# o7 bitches #

import argparse, re, sys, errno, os

parser = argparse.ArgumentParser(description='Cleans nmap output files')
parser.add_argument('-iF', action='store', dest='inputFile', help='nmap ping sweep output file', required=True)
parser.add_argument('-oF', action='store', dest='outputFile', help='Output file for cleaned list')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results = parser.parse_args()

try:
  scanFile = open(results.inputFile, 'r')
except IOError as err:
  print('I/O Error')
  print('Error(' + format(err.errno) + '): ' + format(err.strerror))
else:
  if (results.outputFile):
    try:
      writeFile = open(results.outputFile, 'w')
    except IOError as err:
      print('I/O Error')
      print('Error(' + format(err.errno) + '): ' + format(err.strerror))
    else:
      for line in scanFile:
        if (line.find('host down') < 0 and line.find('latency') < 0 and line.find('packet') < 0):
          ip_candidates = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        if (ip_candidates):
          writeFile.write(ip_candidates[0])
          writeFile.write('\n')
        writeFile.close()
      print ('File Written. Review results in', results.outputFile)
  else:
    for line in scanFile:
      if (line.find('host down') < 0 and line.find('latency') < 0 and line.find('packet') < 0):
        ip_candidates = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        if (ip_candidates):
          print (ip_candidates[0], end='\n')

  scanFile.close()
