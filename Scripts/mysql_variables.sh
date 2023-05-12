#!/bin/bash
# Set up variables for easier access to MySQL binaries mysqld, mysql and mysqladmin.

mysqld="$HOME/bd2_23L_z09_mysql/mysql/bin/mysqld"
mysql="$HOME/bd2_23L_z09_mysql/mysql/bin/mysql --host=localhost --socket=$HOME/bd2_23L_z09_mysql/mysqld.sock"
mysqladmin="$HOME/bd2_23L_z09_mysql/mysql/bin/mysqladmin --host=localhost --socket=$HOME/bd2_23L_z09_mysql/mysqld.sock"
