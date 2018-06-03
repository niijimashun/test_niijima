#!/usr/bin/env python


def plus(a,b):
    return a + b

if __name__=='__main__':
    import sys
    if plus(1,2) !=3:
        sys.exit(0)

    print "hoghoge"
    sys.exit(1)
