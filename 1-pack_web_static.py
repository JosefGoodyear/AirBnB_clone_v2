#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    local("tar -czvf versions/web_static_{}.tgz web_static/".format(time_now))
