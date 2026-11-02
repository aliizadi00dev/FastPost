#!/usr/bin/bash

if [[ ! -d  "/run/postgresql" ]]; then
    sudo mkdir /run/postgresql
    sudo chown $USER:$USER /run/postgresql
fi

pg_ctl -D ./data -l postgres.log start


echo "$(tput setaf 6)"
echo "==========================="
echo "cat postgresql.log:"
echo "$(tput setaf 3)"
cat postgres.log


