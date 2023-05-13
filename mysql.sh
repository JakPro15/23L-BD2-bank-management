#!/bin/bash
# Script for easier MySQL administration

source Scripts/mysql_variables.sh

case $1 in
"")
    $mysql -u bd2-23L-z09 -p;;
"start")
    $mysqld --defaults-file="$HOME/bd2_23L_z09_mysql/mysql_config.cnf" &;;
"stop")
    $mysqladmin -u bd2-23L-z09 -p shutdown;;
*)
    $mysql -u bd2-23L-z09 -p < "$1";;
esac
