#!/usr/bin/python3
"""
Distribute archive to web servers
"""
from fabric.api import put, run, env
import os


env.hosts = ['100.26.210.229', '54.210.107.66']


def do_deploy(archive_path):
    """Distribute archive to web servers
    """
    if not os.path.exists(archive_path):
        return False
    filename = os.path.basename(archive_path)
    tem_archive = "/tmp/{}".format(filename)
    name, ext = os.path.splitext(filename)
    deploy_dir = "/data/web_static/releases/{}".format(name)
    try:
        put(archive_path, tem_archive)
        run("mkdir -p {}".format(deploy_dir))
        run("tar -xzf {} -C {}".format(tem_archive, deploy_dir))
        run("rm {}".format(tem_archive))
        run("mv {}/web_static/* {}/".format(deploy_dir, deploy_dir))
        run("rm -rf {}/web_static".format(deploy_dir))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(deploy_dir))
        return True
    except:
        return False
