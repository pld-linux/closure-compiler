#!/bin/sh
p=closure-compiler
svn=http://$p.googlecode.com/svn/trunk

set -x
set -e
x=$-

# create svn diff and svn log based on revision ranges for each release
svnlogs() {
	set -$x
	local date=$1 range=$2
	test -e log.$date.txt || {
		svn log $svn -r$range > svn.tmp && mv svn.tmp log.$date.txt
	}
	test -e changes.$date.txt || {
		svn diff $svn -r$range > svn.tmp && mv svn.tmp changes.$date.txt
	}
}

svnlogs 20110804 1180:1314
svnlogs 20110811 1314:1346
svnlogs 20111003 1346:1459
svnlogs 20111114 1459:1592
svnlogs 20120123 1592:1741
svnlogs 20120305 1741:1810
svnlogs 20120430 1810:1918
