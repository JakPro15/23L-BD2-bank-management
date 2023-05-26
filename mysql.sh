#!/bin/bash
# Script for easier MySQL administration

source shell_scripts/mysql_variables.sh

check_running()
{
    if ! pgrep -x "mysqld" > /dev/null
    then
        echo "mysqld is not running."
        exit 1
    fi
}

case $1 in
"")
    check_running
    $mysql -u root bd2-23L-z09;;
"start")
    if ! pgrep -x "mysqld" > /dev/null
    then
        $mysqld --defaults-file="$HOME/bd2_23L_z09_mysql/mysql_config.cnf" &
    else
        echo "mysqld is already running."
    fi;;
"stop")
    check_running
    $mysqladmin -u root shutdown;;
*)
    check_running
    $mysql -u root bd2-23L-z09 < "$1";;
esac
