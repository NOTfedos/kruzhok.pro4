#!/usr/bin/env bash

pyv="$(python3 -V 2>&1)"
version=$(echo "$pyv" | grep -Po '(?<=Python )(.+)')
echo "$version"
if [[ -z "$version" ]]
then
    echo "No Python!"
    exit
fi
parsedVersion="${version//./}"

if [[ "$parsedVersion" -lt "300" ]]
then
    echo "Wrong version of Python!"
    exit
fi

python3 -m venv .
source bin/activate
pip3 install requests
chmod 777 ./crawler_tgl.py
