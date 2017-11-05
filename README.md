# Agsub: substitution using ag

## Introduction


`Agsub` is a small python script that extends `ag` (a.k.a. the Silver Searcher) with substitution functionality.

`Ag`, [the Silver Searcher](https://github.com/ggreer/the_silver_searcher), is a fast quasi-drop-in replacement for `grep` that can find all occurences of a regex pattern within a folder. It makes use of multi-core CPUs and is up to orders of magnitude faster than most of its competitors.

Unfortunately `ag` doesn't offer functionality to *replace* occurrences in that file. `Agsub` aims to fill this gap.

**Caution: this script is still very immature. Use at your own risk and make backups of all your files before using this script. I don't take any responsibility if this script damages your computer or your files.**

## Prerequisites
- Python 2.x.
- Ag, the Silver Searcher. For Ubuntu, install with `sudo apt-get install silversearcher-ag`. [**Click here**](https://github.com/ggreer/the_silver_searcher) if you use other distributions.
- [Python `regex` package](https://pypi.python.org/pypi/regex/). Install with command: `pip install regex`. Note this is *not* the built-in package `re`.

## Usage:
1. Put `agsub.py` somewhere and add its location to the PATH environment variable or simply create an alias for this script.
2. Go to the folder where you want to replace all occurrences of a pattern in all files within that folder.
3. `agsub.py <search_pattern> <replacement_pattern>`

Note that the pattern must be valid PCRE regular expression. You can use flags like `(?s)` within the pattern.

## Examples
```
$ cat myfile
abcdefg
hijklmn
opq rst
uvw xyz

$ agsub.py '(\w)(\s)(\w)' '\3\2\1'
Processing myfile ... done

$ cat myfile
abcdefh
gijklmo
npr qsu
tvx wyz
```

## Behind the scene

This script simply calls `ag` with option `-l` to get a list of files that contain the given pattern. After that, it iterates over the files in the list and replaces occurrences of the pattern with the `regex` package by calling `regex.sub`. 

The reason that `regex` is used instead of `re` is that `re` has a far more restricted support for regular expressions than PCRE or `regex` package.


## TODO
- Add support for options that can be passed to `ag`
- Add option for making backups before replacing
- Add tests for various situations