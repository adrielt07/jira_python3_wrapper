#!/usr/bin/env sh

pip3 install -U pip setuptools wheel
pip3 install pex
pip3 wheel -w wheels/ -r requirements.txt .

PYTHON=python3

pex --not-zip-safe --disable-cache --no-pypi -o jiraclient.pex -f wheels/ -m jiraclient.cli:main jiraclient

rm -rf wheel/
