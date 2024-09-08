#!/bin/bash

# release 브랜치 이름을 인자로 받습니다.
release_branch=$1

if [ -z "$release_branch" ]; then
    echo "Usage: $0 <release_branch_name>"
    exit 1
fi

# release 브랜치를 finish 합니다.
git flow release finish -m "Finish release $release_branch" "$release_branch" <<EOF
Merge branch 'release/$release_branch'

This merge is necessary to complete the release process for version $release_branch.
EOF

# develop 브랜치로 전환합니다.
git checkout develop

# develop 브랜치를 원격 저장소에 push 합니다.
git push origin develop

# main 브랜치로 전환합니다.
git checkout main

# main 브랜치를 원격 저장소에 push 합니다.
git push origin main

# 새로 생성된 태그를 원격 저장소에 push 합니다.
git push origin "release/$release_branch"

echo "Release $release_branch has been finished and pushed to remote repository."