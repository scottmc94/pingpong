#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

file = open("games.txt","r")
match = 0
first = ''
second = ''
fwins = 0
swins = 0
date = 0
fin = open("matches.txt","w")
for line in file:
	mysp = line.rstrip('\n').split(",")
	if match != int(mysp[1]):
		if match != 0:
			fin.write('%d,%d,' % (match,match))
			if fwins > swins: fin.write('%s,%s,%s,%d,%d\n' % (first,second,date,fwins,swins))
			if fwins < swins: fin.write('%s,%s,%s,%d,%d\n' % (second,first,date,swins,fwins))
		first = mysp[2] 
		second = mysp[3]
		fwins = 0
		swins = 0
		date = mysp[4]
	if first == mysp[2]:
		fwins += 1
	if first == mysp[3]: 
		swins += 1
	match = int(mysp[1])
file.close()
fin.close()
