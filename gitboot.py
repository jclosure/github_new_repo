
#!/usr/bin/env python
 
import os
import sys

REPO = sys.argv[1]
USER = sys.argv[2]
PASS = sys.argv[3]


print os.system('git init')
print os.system('git add .')
print os.system('git commit -am "initial commit"')
print os.system("curl -u '{USER}:{PASS}' ".format(**vars()) + "https://api.github.com/user/repos -d {" + "'name':'{REPO}'".format(**vars()) + "}")
print os.system("git remote add origin git@github.com:{USER}/{REPO}.git".format(**vars()))
print os.system("git push origin master")


