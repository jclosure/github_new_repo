
#!/usr/bin/env python
 
import os
import sys

REPO = sys.argv[1]
USER = sys.argv[2]
PASS = sys.argv[3]


os.system('git init')
os.system('git add .')
os.system('git commit -am "initial commit"')
os.system("curl -u '{USER}:{PASS}' ".format(**vars()) + "https://api.github.com/user/repos -d {" + "'name':'{REPO}'".format(**vars()) + "}")
os.system("git remote add origin git@github.com:{USER}/{REPO}.git".format(**vars()))
os.system("git push origin master")


