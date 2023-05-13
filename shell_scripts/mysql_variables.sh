#!/bin/bash
# Set up variables for easier access to MySQL binaries mysqld, mysql and mysqladmin.

MYSQL_HOME="$HOME/bd2_23L_z09_mysql"
mysqld="$MYSQL_HOME/mysql/bin/mysqld"
mysql="$MYSQL_HOME/mysql/bin/mysql --host=localhost --socket=$MYSQL_HOME/mysqld.sock"
mysqladmin="$MYSQL_HOME/mysql/bin/mysqladmin --host=localhost --socket=$MYSQL_HOME/mysqld.sock"
