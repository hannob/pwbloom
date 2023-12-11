# pwbloom
Simple web index to use bloom filter for Pwned Passwords

The index.py runs a simple CGI web service checking passwords
with a bloom filter for the Pwned Passwords list.

In addition to this repo you will need:

 * [bloom.py script by Hector Martin](https://gist.github.com/marcan/23e1ec416bf884dcd7f0e635ce5f2724)
 * Bloomfilter file based on [Pwned Passwords list (SHA-1, ordered by hash) by Troy Hunt](https://haveibeenpwned.com/Passwords)

To create the bloomfilter file:

* Get and unpack latest Pwned Passwords list (SHA-1, ordered by hash).

* Count lines (n):

        wc -l [list].txt

* Calculate m [https://krisives.github.io/bloom-calculator/](https://krisives.github.io/bloom-calculator/)
  (for v7 with error p = 0.0005: n = 613584246, m = 9707076175)

* Create filter:

        cat [list].txt | cut -d: -f1 |./bloom.py load -m [m] -k 11 -l passwords-vX.bloom /dev/stdin
