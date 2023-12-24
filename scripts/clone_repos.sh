#!/usr/bin/env bash

USER="CoderContenidos"
URL="https://api.github.com/users/$USER/repos?per_page=1000"
BASE_FOLDER="$HOME/instances/thirdparties/coderhouse"
REPOS=$(curl -s "https://api.github.com/users/${USER}/repos" | jq -r '.[].clone_url')

for repo in $REPOS; do
    repo_name=$(echo $repo | awk -F/ '{print $NF}' | sed 's/\.git$//')
    echo git clone $repo "$BASE_FOLDER/$repo_name"
    git clone $repo "$BASE_FOLDER/$repo_name"
done
