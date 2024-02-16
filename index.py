#!/usr/bin/python3

import hashlib
import os
import sys
import urllib.parse

import bloom

FILTER = "passwords.bloom"

print("Content-type: text/plain")
print("")

if os.environ["REQUEST_METHOD"] != "POST":
    print("error")
    exit()

password = None
for line in sys.stdin.readlines():
    if line.startswith("password="):
        password = line[9:]

if not password:
    print("error")
    exit()

# we need to urldecode POST data
password = urllib.parse.unquote(password)

value = hashlib.sha1(password.encode("utf-8")).hexdigest()

bfilter = bloom.BloomFilter(FILTER, readonly=True)
if bfilter.contains(value):
    print("bad")
else:
    print("good")
