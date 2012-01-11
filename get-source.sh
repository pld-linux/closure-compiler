#!/bin/sh
p=closure-compiler
fn=compiler
svn=http://$p.googlecode.com/svn/trunk
dl=https://code.google.com/p/$p/downloads/list?can=3

set -x
set -e

html() {
	if [ -z "$html" ]; then
		html=$(lynx -width 1200 -dump -nolist "$dl")
	fi
	echo "$html"
}

rev=$(html | perl -ne '/'$fn'-.+tar.*Buil[dt] at r?(\d+)/and print $1')
test -n "$rev"

date=$(html | perl -ne '/'$fn'-(\d+).tar.gz.*Built at r?'$rev'/and print $1')
test -n "$date"

d=$p-$date
if [ ! -d "$d" ]; then
	svn export -q $svn@$rev $p-$date
fi

t=$d.tar.bz2
if [ ! -f "$t" ]; then
	tar -cjf $t --exclude-vcs $d
fi
