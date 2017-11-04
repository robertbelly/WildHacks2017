#!/bin/bash

#!/bin/bash
echo "about to add"
git pull origin master
echo "put string here" >> README.md
git add README.md
git commit -m "this is important ok"
git push origin master
echo "done adding"
