#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from trueskill import Rating, quality_1vs1, rate_1vs1
from collections import defaultdict

#file = open("games.txt","r")
file = open("matches.txt","r")

fn_rating = open("rating.txt","w")

players = {}
report = []
pm = defaultdict(list)
pwin = defaultdict(int)
plos = defaultdict(int)

for line in file:
  mysp = line.rstrip('\n').split(",")
  if mysp[2] not in players: players[mysp[2]] = Rating()
  if mysp[3] not in players: players[mysp[3]] = Rating()
  oldloser = str("%.2f" % players[mysp[3]].mu)
  oldwin = str("%.2f" % players[mysp[2]].mu)
  players[mysp[2]],players[mysp[3]] = rate_1vs1(players[mysp[2]],players[mysp[3]])
  sc = mysp[5]+"-"+mysp[6] 
  wr =  str("%.2f" % players[mysp[2]].mu)
  lr = str("%.2f" % players[mysp[3]].mu)
  pwin[mysp[2]] += 1 
  plos[mysp[3]] += 1 
  pm[mysp[2]].append([int(mysp[0]),mysp[4],mysp[3],oldloser,"W",sc,wr])
  pm[mysp[3]].append([int(mysp[0]),mysp[4],mysp[2],oldwin,"L",sc,lr])

  fn_rating.write('%s,%s,%s,%.2f,%.2f,%s\n' % (mysp[0],mysp[1],mysp[2],players[mysp[2]].mu,players[mysp[2]].sigma, mysp[4]))
  fn_rating.write('%s,%s,%s,%.2f,%.2f,%s\n' % (mysp[0],mysp[1],mysp[3],players[mysp[3]].mu,players[mysp[3]].sigma,mysp[4]))


for key in players:
  report.append((key, players[key].mu, players[key].sigma))

x = 0 
report.sort(key=lambda tup: -tup[1])
fname = "/var/www/pong/index.html"
ht = open(fname,"w")
ht.write("<!DOCTYPE html>\n")
ht.write("<html>\n")
ht.write("<head>\n")
ht.write('<link rel="stylesheet" type="text/css" href="pingpong.css">\n')
ht.write("<title>Ping Pong Ratings</title>\n")
ht.write("</head>\n")
ht.write("<body>\n")
ht.write("<h1>Ratings from Ladder Matches</h1>\n")
ht.write("as of: %s %s vs %s %s-%s<p>\n" % (mysp[4],mysp[2],mysp[3],mysp[5],mysp[6]))
ht.write('<table class="bordered">\n')
ht.write("<thead><tr>\n\t<th>Rank</th>\n\t<th>Name</th>\n\t<th>Record</th>\n\t<th>Rating</th>\n\t<th>Sigma</th>\n</tr></thead>\n")
for rep in report:
  x += 1
  print x,rep[0], "%.2f" % rep[1], "%.2f" % rep[2]
  ht.write("<tr>\n\t<td>%d</td>\n\t<td><a href=%s.html>%s</a></td>\n\t<td>%d-%d</td><td>%.2f</td>\n\t<td>%.2f</td>\n</tr>" % (x,rep[0],rep[0],pwin[rep[0]],plos[rep[0]],rep[1],rep[2]))
ht.write("</table>\n")
ht.write("<p>")
ht.write("Rating value follows player's win/draw/lose records. Higher value means higher game skill. And sigma value follows the number of games. Lower value means many game plays and higher rating confidence </body>\n</html>\n")
ht.close()
fname = None
ht = None



for k in pm:
    pm[k].sort(reverse=True)


for k in pm:
    fname = "/var/www/pong/"+k+".html"
    ht = open(fname,"w")
    ht.write("<!DOCTYPE html>\n")
    ht.write("<html>\n")
    ht.write("<head>\n")
    ht.write('<link rel="stylesheet" type="text/css" href="pingpong.css">\n')
    ht.write("<title>%s games played</title>\n" % k)
    ht.write("</head>\n")
    ht.write("<body>\n")
    ht.write("<h1>%s</h1>\n" % (k))
    ht.write("<h2>Record: %d-%d Rating: %.2f Sigma: %.2f</h2>\n" % (pwin[k],plos[k],players[k].mu,players[k].sigma))
    ht.write('<div align="right"><a href=index.html>Return to Index</a></div>\n')
    ht.write('<table class="bordered">\n')
    ht.write("<thead><tr>\n\t<th>Date</th>\n\t<th>Vs</th>\n\t<th>Result</th>\n\t<th>Score</th>\n\t<th>New Rating</th>\n</tr></thead>\n")
    for j in pm[k]:
        ht.write("<tr>\n\t")
        ht.write("<td>%s</td>\n\t" % j[1])
        ht.write('<td><a href=%s.html>%s</a> (%s)</td>\n\t' % (j[2],j[2],j[3]))
        ht.write("<td>%s</td>\n\t" % j[4])
        ht.write("<td>%s</td>\n\t" % j[5])
        ht.write("<td>%s</td>\n\t" % j[6])
        ht.write("</tr>\n")
    ht.write("</table>\n")
    ht.write('<div align="right"><a href=index.html>Return to Index</a></div>\n')
    ht.write("</body>\n</html>\n")
    ht.close()
    fname = None
    ht = None

fn_rating.close()
file.close()
