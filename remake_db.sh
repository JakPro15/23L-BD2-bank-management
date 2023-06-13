#!/bin/bash

./mysql.sh sql_scripts/drops.sql &&
./mysql.sh sql_scripts/setup_database.sql &&
./mysql.sh sql_scripts/data_creation.sql &&
./mysql.sh sql_scripts/procedures_functions.sql
