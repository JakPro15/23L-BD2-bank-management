#!/bin/bash
# Install and set up MySQL database

cd $(dirname "$0")
source shell_scripts/mysql_variables.sh

if [ "$1" = "clean" ];
then
    if pgrep -x "mysqld" > /dev/null
    then
        $mysqladmin -u bd2-23L-z09 -pbd2 shutdown
    fi
    rm -rf "$MYSQL_HOME/mysql" 2> /dev/null
    rm "$MYSQL_HOME/mysql_config.cnf" 2> /dev/null
    exit 0
fi

if [ ! -f $mysqld ];
then
    if [ ! -f "$MYSQL_HOME/mysql.tar.xz" ];
    then
        echo "Downloading MySQL archive"
        mkdir "$MYSQL_HOME"
        if [ $(uname -m | grep '64') != "" ];
        then
            wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.31-linux-glibc2.12-x86_64.tar.xz \
                -O ~/bd2_23L_z09_mysql/mysql.tar.xz
        else
            wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.31-linux-glibc2.12-i686.tar.xz \
                -O ~/bd2_23L_z09_mysql/mysql.tar.xz
        fi
    fi
    echo "Unzipping MySQL archive"
    tar -xf "$MYSQL_HOME/mysql.tar.xz" -C "$MYSQL_HOME"
    if [ -d "$MYSQL_HOME/mysql-8.0.31-linux-glibc2.12-i686" ];
    then
        mv "$MYSQL_HOME/mysql-8.0.31-linux-glibc2.12-i686" "$MYSQL_HOME/mysql"
    else
        mv "$MYSQL_HOME/mysql-8.0.31-linux-glibc2.12-x86_64" "$MYSQL_HOME/mysql"
    fi
    echo "Finished"
    if [ ! -f $mysqld ];
    then
        echo "Failed to unzip the MySQL archive."
        exit 1
    fi
    echo "Setting up MySQL"
    # prepare MySQL configuration file
    cp others/mysql_config.cnf "$MYSQL_HOME"
    sed -i "s#HOME#$HOME#" "$MYSQL_HOME/mysql_config.cnf"
    sed -i "s#USER#$USER#" "$MYSQL_HOME/mysql_config.cnf"
fi
$mysqld --initialize-insecure --datadir="$MYSQL_HOME/mysql/data"
# launch MySQL
$mysqld --defaults-file="$MYSQL_HOME/mysql_config.cnf" &
sleep 2
# set up user and database
$mysql -u root < sql_scripts/setup_user.sql
$mysql -u bd2-23L-z09 -pbd2 < sql_scripts/setup_database.sql

$mysqladmin -u bd2-23L-z09 -pbd2 shutdown
