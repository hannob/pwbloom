# pwbloom
Simple web index to use bloom filter for Pwned Passwords

The index.py runs a simple CGI web service checking passwords with a bloom filter for
the Pwned Passwords list. It uses the [bloom.py script by Hector Martin](
https://gist.github.com/marcan/23e1ec416bf884dcd7f0e635ce5f2724). A copy is included in
this repo.

In addition, you will need:

* 
* Bloomfilter file based on [Pwned Passwords list (SHA-1, ordered by hash) by Troy
  Hunt](https://haveibeenpwned.com/Passwords). Unfortunately, a simple download of the
  Pwned Passwords list is no longer available. The [last version can be found at the
  Internet Archive](https://archive.org/details/pwned-passwords-version-8).

To create the bloomfilter file:

* Get and unpack the latest Pwned Passwords list (SHA-1, ordered by hash).

* Count lines (n):

        wc -l [list].txt

* Calculate m [https://krisives.github.io/bloom-calculator/](
  https://krisives.github.io/bloom-calculator/).

* Create filter:

        cat [list].txt | cut -d: -f1 |./bloom.py load -m [m] -k 11 -l passwords-vX.bloom /dev/stdin

Example values:

|    | error (p) | count (n) | functions (k) | size (m)    |
| -- | --------- | --------- | ------------- | ----------- |
| v7 | 0.0005    | 613584246 | 10.96 (~11)   |  9707076175 |
| v7 | 0.00005   | 613584246 | 14.28 (~14)   | 12647696584 |
| v8 | 0.0005    | 847223402 | 10.96 (~11)   | 13403313651 |
| v8 | 0.00005   | 847223402 | 14.28 (~14)   | 17463656535 |
