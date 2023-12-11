#!/usr/bin/python3

import hashlib
import sys

import bloom

FILTER = "passwords-v7.bloom"

print("Content-type: text/plain")
print("")

password = None
for line in sys.stdin.readlines():
    if line.startswith("password="):
        password = line[9:]

if not password:
    print("error")
    exit()

value = hashlib.sha1(password.encode("utf-8")).hexdigest()

bfilter = bloom.BloomFilter(FILTER, readonly=True)
if bfilter.contains(value):
    print("bad")
else:
    print("good")
