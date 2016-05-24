#! /usr/bin/env python
def foo():
    #print '\ncalling foo()...'
    aString = 'bar'
    anInt = 42
    print ('foo()'s globals:',globals().keys())
    print ("foo()'s locals:",locals().keys())
print ("_main_'s globals:",globals().keys())
print ("_main_'s locals:",locals().keys())
foo()