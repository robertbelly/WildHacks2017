#!/bin/bash

echo "about to add"
git pull origin master

tmp_pass=0
if [ $tmp_pass = 0 ]; then
        tmp_pass=`head -c 10 /dev/random | base64`
        echo "${tmp_pass:0:10}" #cut to 10 characters after base64 conversion
fi

echo "$tmp_pass" >> README.md
git add README.md
git commit -m "this is important ok"
git push origin master
echo "done adding"
