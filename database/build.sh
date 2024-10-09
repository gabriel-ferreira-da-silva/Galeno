#!/bin/bash

DB_NAME="galeno_database"
COLLECTION_NAME="models"

collection_exists=$(mongosh --quiet --eval "db.getSiblingDB('$DB_NAME').getCollectionNames().indexOf('$COLLECTION_NAME') >= 0")

echo $collection_exists

if [ "$collection_exists" == "true" ]; then
  echo "Collection $COLLECTION_NAME exist."
  exit 1
else
  echo "Collection $COLLECTION_NAME does not exist."
  mongosh --file setup_database.gal.js
  exit 0
fi