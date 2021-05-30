#!/bin/bash
set -e

# Copyright 2021 Hayden Young. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

echo "Waiting for database up..."

while ! nc -z $DATABASE_HOST 5432; do
    sleep 0.1
done

echo "Database up"

exec "$@"