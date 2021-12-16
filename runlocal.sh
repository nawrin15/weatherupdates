#!/bin/bash
localEnv=localdev

envFile=./.env
appFilesDir=./deploy/app

source runlocalscriptutil/getvaluefromconfigfile.sh

echo 'Reading config file...'
dbName=$(getValueFromConfigFile DB_NAME)
dbUser=$(getValueFromConfigFile DB_USER)
dbPassword=$(getValueFromConfigFile DB_PASSWORD)
dbPort=$(getValueFromConfigFile DB_PORT)

echo "Setup environment variable file"
rm -rf .env
touch .env
echo "WEATHER_UPDATES_DB_NAME="$dbName >> $envFile
echo "WEATHER_UPDATES_DB_USER="$dbUser >> $envFile
echo "WEATHER_UPDATES_DB_PASSWORD="$dbPassword >> $envFile
echo "WEATHER_UPDATES_DB_PORT="$dbPort >> $envFile

cat $envFile

echo "Setup Docker/Docker compose files for local $localEnv"
cp $appFilesDir/$localEnv/"$localEnv"compile.sh ./www/compile.sh
cp $appFilesDir/Dockerfile ./
cp $appFilesDir/docker-compose.yml ./

echo "Set file permission"
chmod 755 ./www/compile.sh

python3 $appFilesDir/generaterequirements.py $localEnv > requirements.txt


echo "Staring Docker locally with docker-compose"
sudo docker-compose up --build

echo "Cleaning up env file...."
rm -rf $envFile

echo "Cleaning up local deploy files after runlocal"
rm -rf ./www/compile.sh
rm -rf ./requirements.txt
rm -rf ./Dockerfile
rm -rf ./docker-compose.yml
