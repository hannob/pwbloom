# pwbloom
Simple web index to use bloom filter for Pwned Passwords

The index.py runs a simple CGI web service checking passwords with a bloom filter for
the Pwned Passwords list.

In addition to this repo you will need:

* [bloom.py script by Hector Martin](
  https://gist.github.com/marcan/23e1ec416bf884dcd7f0e635ce5f2724)
* Bloomfilter file based on [Pwned Passwords list (SHA-1, ordered by hash) by Troy
  Hunt](https://haveibeenpwned.com/Passwords) (unfortunately, a simple download of the
  Pwned Passwords list is no longer available, the [last version can be found at the
  Internet Archive](https://archive.org/details/pwned-passwords-version-8).

To create the bloomfilter file:

* Get and unpack latest Pwned Passwords list (SHA-1, ordered by hash).

* Count lines (n):

        wc -l [list].txt

* Calculate m [https://krisives.github.io/bloom-calculator/](
  https://krisives.github.io/bloom-calculator/) (with error p = 0.0005, for v7 n =
  613584246, m = 9707076175, k = 11, for v8 n = 847223402, m = 13403313651, k = 11)

* Create filter:

        cat [list].txt | cut -d: -f1 |./bloom.py load -m [m] -k 11 -l passwords-vX.bloom /dev/stdin
