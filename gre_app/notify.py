#!usr/bin/env python

import pynotify
import time

fr = open("random.txt")
lines = fr.readlines()
num = len(lines)
#print lines

for i in range(num):
    pynotify.init("Test")
    notice = pynotify.Notification("Note",lines[i])
    notice.show()
    if i==num:
        i=0
