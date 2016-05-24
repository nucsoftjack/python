#! /python
from time import ctime, sleep

def tsfunc(func):
    def wrappedFunc():
	    print '[%s] %s() called'% (ctime(),func._name_)
	    return func()
    return wrappedFunc
@tsfunc
def foo():
    pass
    
foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()