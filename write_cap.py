from os import listdir, rename
from os.path import isfile, join

cap = "6"
new = 1
old = 0
for f in listdir(cap):
    if isfile(join(cap, f)):
        new_file_name = f.replace(str(old), str(new))
        rename(join(cap, f), new_file_name)
        old += 1
        new += 1
