#!/bin/bash
# Check whether Python and MySQL are installed.

source Scripts/mysql_variables.sh

if ! which python3 >>/dev/null; then
    echo "Python3 needs to be installed to launch the program."
    exit 1
fi

if [ ! -f $mysqld ]; then
    echo "MySQL server needs to be installed to launch the program."
    exit 1
fi
