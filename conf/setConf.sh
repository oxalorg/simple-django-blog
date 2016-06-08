#!/usr/bin/env sh

basedir=`pwd`
confdir=$basedir
projname=earthlyhumans.com
nginxdir=/etc/nginx/sites-available
vassaldir=/etc/uwsgi/vassals

sudo cp -iv $confdir/$projname.conf $nginxdir/$projname.conf
sudo cp -iv $confdir/$projname.uwsgi.ini $vassaldir/$projname.uwsgi.ini

# restart the uwsgi vassal process
sudo touch $vassaldir/$projname.uwsgi.ini || echo "uwsgi touch failed."

# check nginx config and restart
sudo nginx -t && echo "Now RUN: sudo service nginx restart" || echo "nginx config error"
