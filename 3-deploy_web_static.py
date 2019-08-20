#!/usr/bin/python3
# script for a full deployment
from fabric.api import *
from datetime import datetime
import os


env.hosts = ['34.74.63.236', '35.237.173.143']


def deploy():
    """ run do_pack and do_deploy """
    archive = do_pack()
    if archive is None:
        return False
    res = do_deploy(archive)
    return res


def do_pack():
    """ archive web_static """
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    check = local("tar -czvf versions/web_static_{}.tgz web_static/"
                  .format(time_now))
    if check.succeeded:
        return "versions/web_static_{}.tgz".format(time_now)
    return None


def do_deploy(archive_path):
    """ deploy the archived file to your server """
    chk = True
    if not os.path.exists(archive_path):
        chk = False
    chk = put(archive_path, '/tmp/')
    if chk.failed:
        chk = False
    relative_file = archive_path.rsplit('/', 1)[-1]
    remote_directory = relative_file.rsplit('.')[0]
    chk = run('mkdir -p /data/web_static/releases/{}/'
              .format(remote_directory))
    if chk.failed:
        chk = False
    chk = run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
              .format(relative_file, remote_directory))
    if chk.failed:
        chk = False
    chk = run('rm /tmp/{}'.format(relative_file))
    if chk.failed:
        chk = False
    chk = run('mv /data/web_static/releases/' +
              remote_directory +
              '/web_static/* /data/web_static/releases/' +
              remote_directory + '/')
    if chk.failed:
        chk = False
    chk = run('rm -rf /data/web_static/releases/{}/web_static'
              .format(remote_directory))
    if chk.failed:
        chk = False
    chk = run('rm -rf /data/web_static/current')
    if chk.failed:
        chk = False
    chk = run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
              .format(remote_directory))
    if chk.failed:
        chk = False
    return chk
