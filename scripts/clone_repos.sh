#!/usr/bin/env bash

USER="CoderContenidos"
URL="https://api.github.com/users/$USER/repos?per_page=1000"
BASE_FOLDER="$HOME/instances/thirdparties/coderhouse"
REPOS=$(curl -s "$URL" | grep -o 'git://[^"]*')

for repo in $REPOS; do
    repo_name=$(echo $repo | awk -F/ '{print $NF}' | sed 's/\.git$//')
    git clone $repo "$BASE_FOLDER/$repo_name"
done
