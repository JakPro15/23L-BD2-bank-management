#!/bin/bash
# Install and set up MySQL database

cd $(dirname "$0")

source Scripts/mysql_variables.sh

if [ ! -f $mysqld ];
then
    if [ ! -f "$HOME/bd2_23L_z09_mysql/mysql.tar.xz" ];
    then
        echo "MySQL archive needs to be downloaded to '~/bd2_23L_z09_mysql' under the name 'mysql.tar.xz'"
        exit 1
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
$mysql -u bd2-23L-z09 -pbd2.2023.BD2 < Scripts/setup_database.sql

$mysqladmin -u root shutdown
