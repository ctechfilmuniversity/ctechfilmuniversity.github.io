import sys;

from os import walk


print(sys.version)


f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    print(filenames)
    f.extend(filenames)
    break