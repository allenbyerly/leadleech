#!/bin/sh
cd -- "$(dirname "$BASH_SOURCE")"

#Activate vitrual environment
source env/bin/activate

python leadleech.py

deactivate
