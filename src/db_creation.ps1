# On this file you'll find the script to connect to database using the databse mangement tool PostgreSQL 
$USER = Read-Host "Please, enter your username of PostgreSQL:"

$PASSWORD = Read-Host "Please, enter your password of PostgreSQL:" -AsSecureString # This will ensure that the password wont be shown during typing

$SERVER_ = Read-Host "Please, enter your server name of PostgreSQL:"

$PORT_ = Read-Host "Please, enter your port of PostgreSQL:" # Normally this will be 5432 but you can check on pgAdmin if the port is different 

$DB_NAME = Read-Host "Please, enter the name of the database you want to create:"

$SCHEMA_NAME = Read-Host "Please, enter the name of the schema you want to create:"

# Now we need to create a command to create the database will use the following
$env:PGPASSWORD = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($PASSWORD))
psql -U $USER -h $SERVER_ -p $PORT_ -c "Create database $DB_NAME;" 

# Command to create the schema
psql -U $USER -h $SERVER_ -p $PORT_ -d $DB_NAME -c "Create Schema $SCHEMA_NAME;"

# Ask the user if he would like to grant another user priviliges
$GRANT_PRIVILIGES = Read-Host "Would you like to grant writing and reading priviliges to other user? (y/n)"

if ($GRANT_PRIVILIGES -eq "y"){
    $OTHER_USER = Read-Host "Please provide the name of the user you would grant priviliges:"
    psql -U $USER -h $SERVER_ -p $PORT_ -d $DB_NAME -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME to $OTHER_USER;"
    psql -U $USER -h $SERVER_ -p $PORT_ -d $DB_NAME -c "GRANT ALL PRIVILEGES ON SCHEMA $SCHEMA_NAME to $OTHER_USER;"
}