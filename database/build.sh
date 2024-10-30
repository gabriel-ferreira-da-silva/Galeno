#!/bin/bash

DB_NAME="galeno_database"
COLLECTION_NAME="models"

# Check if the collection exists
collection_exists=$(mongosh --quiet --eval "db.getSiblingDB('$DB_NAME').getCollectionNames().indexOf('$COLLECTION_NAME') >= 0")

echo "Collection exists: $collection_exists"

if [ "$collection_exists" == "true" ]; then
  echo "Collection $COLLECTION_NAME exists."
else
  echo "Collection $COLLECTION_NAME does not exist."
  mongosh --file setup_database.gal.js

  if [ $? -ne 0 ]; then
    echo "Failed to set up the database."
    exit 1
  fi
fi

# Change to mlmodels directory and run the build script
cd mlmodels || { echo "Failed to change directory to mlmodels"; exit 1; }
echo "Running build.sh in mlmodels directory..."
./build.sh

# Check if the build script executed successfully
if [ $? -eq 0 ]; then
  echo "Inserted models successfully."
else
  echo "Failed to run build.sh."
  exit 1
fi

cd ..
