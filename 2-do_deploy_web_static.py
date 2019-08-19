#!/usr/bin/python3
""" deploy the archived file to your server """
import os
from fabric.api import *

env.hosts = ['34.74.63.236', '35.237.173.143']


def do_deploy(archive_path):
    """ deploy the archived file to your server """
    if not os.path.exists(archive_path):
        return False
    chk = put(archive_path, '/tmp/')
    if chk.failed:
        return False
    relative_file = archive_path.rsplit('/', 1)[-1]
    remote_directory = relative_file.rsplit('.')[0]

    chk = run('mkdir -p /data/web_static/releases/{}/'
              .format(remote_directory))
    if chk.failed:
        return False
    chk = run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
              .format(relative_file, remote_directory))
    if chk.failed:
        return False
    chk = run('rm /tmp/{}'.format(relative_file))
    if chk.failed:
        return False
    chk = run('mv /data/web_static/releases/' +
              remote_directory +
              '/web_static/* /data/web_static/releases/' +
              remote_directory + '/')
    if chk.failed:
        return False
    chk = run('rm -rf /data/web_static/releases/{}/web_static'
              .format(remote_directory))
    if chk.failed:
        return False
    chk = run('rm -rf /data/web_static/current')
    if chk.failed:
        return False
    chk = run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
              .format(remote_directory))
    if chk.failed:
        return False
    return True
