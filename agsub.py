#!/usr/bin/env python
import sys
import regex
import subprocess

if __name__ == '__main__':
    assert len(sys.argv) == 3

    try:
        names = subprocess.check_output(['ag', '-l', sys.argv[1]])
        names = filter(None, names.split('\n'))
    except OSError, e:
        print 'ag (silver searcher) must be installed and present in PATH.'
        exit(1)
    except subprocess.CalledProcessError, e:
        exit(2)

    for fname in names:
        print 'Processing', fname, '...',
        content = open(fname, 'rb').read()
        result = regex.sub(sys.argv[1], sys.argv[2], content)
        with open(fname, 'wb') as fout:
            fout.write(result)
            print 'done'
