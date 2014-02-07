#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


from trueskill import Rating, quality_1vs1, rate_1vs1
players = {}
report = []

players['asmith'] = Rating()
players['atoumey']= Rating()
players['cbrake'] = Rating()
players['cdunbar'] = Rating()
players['drichardson'] = Rating()
players['dtoumey'] = Rating()
players['jenders'] = Rating()
players['jgoller'] = Rating()
players['jgross'] = Rating()
players['jklee'] = Rating()
players['jroberts'] = Rating()
players['jshaffer'] = Rating()
players['kmoore'] = Rating()
players['mhodson'] = Rating()
players['mkussow'] = Rating()
players['mmesser'] = Rating()
players['mparker'] = Rating()
players['mrowe'] = Rating()
players['msamples'] = Rating()
players['mweston'] = Rating()
players['smcpheeters'] = Rating()
players['sshepherd'] = Rating()
players['wnorton'] = Rating()
#players['neverplayed'] = Rating()

file = open("games.txt","r")

for line in file:
  mysp = line.rstrip('\n').split(",")
  players[mysp[2]],players[mysp[3]] = rate_1vs1(players[mysp[2]],players[mysp[3]])
  print mysp[0],mysp[1],mysp[2], "%.2f" % players[mysp[2]].mu, "%.2f" % players[mysp[2]].sigma, mysp[4]
  print mysp[0],mysp[1],mysp[3],"%.2f" % players[mysp[3]].mu, "%.2f" % players[mysp[3]].sigma,mysp[4]


for key in players:
  report.append((key, players[key].mu, players[key].sigma))

x = 0 
report.sort(key=lambda tup: -tup[1])
for rep in report:
  x += 1
  print x,rep[0], "%.2f" % rep[1], "%.2f" % rep[2]

#x = 0
#for rep in report:
#  if x == 0: 
#    print rep[0]," vs ",
#    x = 1
#  else:
#    print rep[0]
#    x = 0
#
#print
#print
#for rep in report:
#  print rep[0]+";",
#print  quality_1vs1(players['mmesser'],players['msamples'])
#print  quality_1vs1(players['sshepherd'],players['dtoumey'])

