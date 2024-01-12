#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""
do_pack = __import__('1-pack_web_static')
do_deploy = __import__('2-do_deploy_web_static')

def deploy():
    """creates and distributes an archive to the web servers"""
    path_web = do_pack()
    if path_web is None:
        return False
    return do_deploy(path_web)
