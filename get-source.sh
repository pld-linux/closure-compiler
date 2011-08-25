#!/bin/sh
p=closure-compiler
fn=compiler
svn=http://$p.googlecode.com/svn/trunk
dl=https://code.google.com/p/$p/downloads/list?can=3

set -x

html() {
	if [ -z "$html" ]; then
		html=$(lynx -width 1200 -dump -nolist "$dl")
	fi
	echo "$html"
}

rev=$(html | perl -nne '/'$fn'-latest.tar.gz.*Build at r(\d+)/and print $1')
date=$(html | perl -ne '/'$fn'-(\d+).tar.gz.*Build at r'$rev'/and print $1')

d=$p-$date
if [ ! -d "$d" ]; then
	svn export -q $svn@$rev $p-$date
fi

t=$d.tar.bz2
if [ ! -f "$t" ]; then
	tar -cjf $t --exclude-vcs $d
fi
