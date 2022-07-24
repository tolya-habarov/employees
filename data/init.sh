#!/bin/bash

mongoimport --username ${MONGO_INITDB_ROOT_USERNAME} --password ${MONGO_INITDB_ROOT_PASSWORD} --authenticationDatabase admin --jsonArray --db ${MONGO_INITDB_DATABASE} --collection employees < /tmp/employees.json
