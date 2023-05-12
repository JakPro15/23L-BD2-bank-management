#!/bin/bash
# Install and set up MySQL database

cd $(dirname "$0")
source Scripts/mysql_variables.sh

if [ "$1" = "clean" ];
then
    rm -rf "$HOME/bd2_23L_z09_mysql/mysql" 2> /dev/null
    rm "$HOME/bd2_23L_z09_mysql/mysql_config.cnf" 2> /dev/null
    exit 0
fi

if [ ! -f $mysqld ];
then
    if [ ! -f "$HOME/bd2_23L_z09_mysql/mysql.tar.xz" ];
    then
        echo "Downloading MySQL archive"
        mkdir ~/bd2_23L_z09_mysql
        if [ $(uname -m | grep '64') != "" ];
        then
            wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.31-linux-glibc2.12-x86_64.tar.xz -O ~/bd2_23L_z09_mysql/mysql.tar.xz
        else
            wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.31-linux-glibc2.12-i686.tar.xz -O ~/bd2_23L_z09_mysql/mysql.tar.xz
        fi
    fi
    echo "Unzipping MySQL archive"
    tar -xf "$HOME/bd2_23L_z09_mysql/mysql.tar.xz" -C "$HOME/bd2_23L_z09_mysql"
    if [ -d "$HOME/bd2_23L_z09_mysql/mysql-8.0.31-linux-glibc2.12-i686" ];
    then
        mv "$HOME/bd2_23L_z09_mysql/mysql-8.0.31-linux-glibc2.12-i686" "$HOME/bd2_23L_z09_mysql/mysql"
    else
        mv "$HOME/bd2_23L_z09_mysql/mysql-8.0.31-linux-glibc2.12-x86_64" "$HOME/bd2_23L_z09_mysql/mysql"
    fi
    echo "Finished"
    if [ ! -f $mysqld ];
    then
        echo "Failed to unzip the MySQL archive."
        exit 1
    fi
    echo "Setting up MySQL"
    # prepare MySQL configuration file
    cp Others/mysql_config.cnf "$HOME/bd2_23L_z09_mysql"
    sed -i "s#HOME#$HOME#" "$HOME/bd2_23L_z09_mysql/mysql_config.cnf"
    sed -i "s#USER#$USER#" "$HOME/bd2_23L_z09_mysql/mysql_config.cnf"
fi
$mysqld --initialize-insecure --datadir="$HOME/bd2_23L_z09_mysql/mysql/data"
# launch MySQL
$mysqld --defaults-file="$HOME/bd2_23L_z09_mysql/mysql_config.cnf" &
sleep 2
# set up user and database
$mysql -u root < Scripts/setup_user.sql
$mysql -u bd2-23L-z09 -pbd2 < Scripts/setup_database.sql

$mysqladmin -u bd2-23L-z09 -pbd2 shutdown
