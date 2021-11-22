#!/usr/bin/python3

import hashlib
import cgi
import bloom

FILTER = "passwords-v7.bloom"

print("Content-type:text/plain")
print("")

password = cgi.FieldStorage(environ={'REQUEST_METHOD': 'POST'}).getvalue("password")
if not password:
    print("error")
    exit()

value = hashlib.sha1(password.encode('utf-8')).hexdigest()

bfilter = bloom.BloomFilter(FILTER, readonly=True)
if bfilter.contains(value):
    print("bad")
else:
    print("good")
