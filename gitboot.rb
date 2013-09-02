#!/usr/bin/env ruby

REPO = ARGV[0] || "MONKEY"
USER = ARGV[1] || "jclosure"
PASS = ARGV[2] || "xxxxxxxxx"

# REPO = ARGV[0]
# USER = ARGV[1]
# PASS = ARGV[2]


p system('git init')
p system('git add .')
p system('git commit -am "initial commit"')
p system("curl -u '#{USER}:#{PASS}' https://api.github.com/user/repos -d '{\"name\":\"#{REPO}\"}'")
p system("git remote add origin git@github.com:#{USER}/#{REPO}.git")
p system("git push origin master")
