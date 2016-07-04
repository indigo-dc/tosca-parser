#!/bin/bash

apt update
apt install -y python-stdeb
python setup.py --command-packages=stdeb.command sdist_dsc --depends "python-pbr, python-dateutil" bdist_deb
mkdir dist_pkg
cp deb_dist/*.deb dist_pkg