#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

while ! mysqladmin ping -h"$SQL_HOST" --silent; do
    sleep 1
done

exec "$@"
