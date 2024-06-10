#!/bin/bash

# Ask the user the username to use
echo "Please, enter your username of PostgreSQL:"
read USER

# Ask the user for his password
echo "Please, enter your password of PostgreSQL:"
read -s PASSWORD

# Ask the user for the host name
echo "Por favor, ingresa el nombre del host:"
read HOST_

# Ask the user the db port
echo "Please, enter your port of PostgreSQL:"
read PORT_

# Ask the user the database name
echo "Please, enter the name of the database you want to create:"
read DB_NAME

# Ask the user the schema name
echo "Please, enter the name of the schema you want to create:"
read SCHEMA_NAME

# Comand to create the database
PGPASSWORD=$PASSWORD psql -U $USER -h $HOST_ -p $PORT_ -c "CREATE DATABASE $DB_NAME;"

# Comand to create the schema
PGPASSWORD=$PASSWORD psql -U $USER -h $HOST_ -p $PORT_ -d $DB_NAME -c "CREATE SCHEMA $SCHEMA_NAME;"

# Ask the user the user if he would grant priviliges to other users
echo "Would you like to grant priviliges to other users? (y/n)"
read GRANT_PRIVILEGES

if [ "$GRANT_PRIVILEGES" = "y" ]; then
    echo "Please type the name of the user to grant privileges"
    read OTHER_USER
    PGPASSWORD=$PASSWORD psql -U $USER -h $HOST_ -p $PORT_ -d $DB_NAME -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $OTHER_USER;"
    PGPASSWORD=$PASSWORD psql -U $USER -h $HOST_ -p $PORT_ -d $DB_NAME -c "GRANT ALL PRIVILEGES ON SCHEMA $SCHEMA_NAME TO $OTHER_USER;"
fi