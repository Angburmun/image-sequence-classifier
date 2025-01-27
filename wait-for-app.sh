#!/bin/bash
# wait-for-app.sh

set -e

host="$1"
shift
cmd="$@"

until curl -s "$host" > /dev/null; do
  echo "Waiting for app..."
  sleep 2
done

exec $cmd
