import sys;

from os import walk


print("Starting to look for new or updated content")


f = []
for (dirpath, dirnames, filenames) in walk("__content/"):
    print(dirpath)
    print(dirnames)
    print(filenames)
    f.extend(filenames)
    break