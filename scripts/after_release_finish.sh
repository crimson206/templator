#!/bin/bash

release_tag=$1

if [ -z "$release_tag" ]; then
    echo "Usage: $0 <release_branch_name>"
    exit 1
fi

# develop 브랜치로 전환합니다.
git checkout develop

# develop 브랜치를 원격 저장소에 push 합니다.
git push origin develop

# main 브랜치로 전환합니다.
git checkout main

# main 브랜치를 원격 저장소에 push 합니다.
git push origin main

# 새로 생성된 태그를 원격 저장소에 push 합니다.
git push origin "$release_tag"

echo "Release $release_tag has been finished and pushed to remote repository."