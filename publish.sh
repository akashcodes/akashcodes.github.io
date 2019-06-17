#!/usr/bin/bash
source ../venv/pelican/bin/activate
pelican content -o output -s pelicanconf.py
ghp-import output -r origin -b master
git push origin master
git checkout pelican
exec bash