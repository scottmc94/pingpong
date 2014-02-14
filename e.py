#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#read the file
#save the gameid
#save the matchid
#save array of players
#Ask:
#Winner?
#Check against array, if found go else verify
#Loser?
#Wins?
#if wins 3 put in 3 games.
#If wins 2, ask which game lost.
#

import time

file = open("games.txt","r")
players = []
m = []
for line in file:
	m = line.rstrip('\n').split(",")
	gameid = m[0]
	matchid = m[1]
	players.append(m[2])
	players.append(m[3])

players = list(set(players))
print "Last game entered: %s %s %s vs %s %s" % (m[0],m[1],m[2],m[3],m[4])
x = 0
while x == 0:
	winner = raw_input('Enter Winner: ')
	if winner not in players:
		ans = raw_input(winner + ' Does not exist, OK? (Y)/N ')
		if ans.lower() != 'n':
			x = 1
	else:
		x = 1	

x = 0
while x == 0:
	loser = raw_input('Enter Loser: ')
	if loser not in players:
		ans = raw_input(loser + ' Does not exist, OK? (Y)/N ')
		if ans.lower() != 'n':
			x = 1
	else:
		x = 1

wins = int(raw_input('Enter Wins: (3 or 2) '))
if wins == 2:
	loses = int(raw_input('Which game lost?: (1,2,3) '))
else:
	loses = 0

ans = raw_input('Is this date correct? ' + time.strftime("%Y-%m-%d") + ' (Y)/N ')
if ans.lower() == 'n':
	mydate = raw_input('Enter date YYYY-MM-DD: ')
else:
	mydate = time.strftime("%Y-%m-%d")

file.close()
file = open("games.txt","a")
gameid = int(gameid)
matchid = int(matchid)
matchid += 1
print "Adding match data to games.txt"
for x in range(1,4):
	gameid += 1
	if loses == x:
		print '%d,%d,%s,%s,%s' % (gameid,matchid,loser,winner,mydate)
		file.write ('%d,%d,%s,%s,%s\n' % (gameid,matchid,loser,winner,mydate))
	else:
		print '%d,%d,%s,%s,%s' % (gameid,matchid,winner,loser,mydate)
		file.write ('%d,%d,%s,%s,%s\n' % (gameid,matchid,winner,loser,mydate))
file.close()


