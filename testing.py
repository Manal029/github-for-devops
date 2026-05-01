import os

os.system("git add .")
os.system('git commit -m "update files"')
os.system("git pull origin master --rebase")
os.system("git push origin master")