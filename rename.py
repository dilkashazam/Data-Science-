from os import walk
from os import rename

mypath = 'XYZ'
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    for fileN in filenames:
        rename(mypath+'/'+fileN, mypath+'/'+mypath + '_' + fileN)