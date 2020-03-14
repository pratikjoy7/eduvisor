#!/bin/sh

echo Database host - $MYSQL_HOST

while ! curl mysql:3306
do
  echo "$(date) - still trying"
  sleep 1
done

echo "$(date) - connected successfully"

python3 eduvisor/admin/server.py
