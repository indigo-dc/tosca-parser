#!/bin/bash

yum -y install rpm-build python-setuptools
echo "%_unpackaged_files_terminate_build 0" > ~/.rpmmacros
python setup.py bdist_rpm --requires="python-pbr, python-dateutil"
mkdir dist_pkg
cp dist/*.noarch.rpm dist_pkg