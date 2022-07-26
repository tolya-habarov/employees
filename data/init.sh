#!/bin/bash

mongoimport \
    --username ${MONGO_INITDB_ROOT_USERNAME} \
    --password ${MONGO_INITDB_ROOT_PASSWORD} \
    --authenticationDatabase admin \
    --jsonArray \
    --db ${MONGO_INITDB_DATABASE} \
    --collection employees < /tmp/employees.json && \
mongo \
    --username ${MONGO_INITDB_ROOT_USERNAME} \
    --password ${MONGO_INITDB_ROOT_PASSWORD} <<EOF
    use $MONGO_INITDB_DATABASE;
    db.employees.updateMany(
        {},
        [
            {
                \$set: { join_date: { \$dateFromString: { dateString: "\$join_date" } } }
            }
        ]
    );
EOF