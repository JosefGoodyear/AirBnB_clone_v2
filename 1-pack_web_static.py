#!/usr/bin/python3
""" archive web_static for easy shipping """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ archive web_static """
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    check = local("tar -czvf versions/web_static_{}.tgz web_static/"
                  .format(time_now))
    if check.succeeded:
        return check
