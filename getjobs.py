#! /usr/bin/python
import urllib;
f = urllib.urlopen("www.google.com/jobs");
buf = f.read();
f.close();
print buf;
