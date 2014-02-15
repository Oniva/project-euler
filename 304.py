# This file was *autogenerated* from the file 304.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_5 = Integer(5); _sage_const_1234567891011 = Integer(1234567891011); _sage_const_10 = Integer(10); _sage_const_14 = Integer(14)
GF = Integers(_sage_const_1234567891011 )

def fib(x) :
    a = matrix(GF, [_sage_const_0 , _sage_const_1 ])
    b = matrix(GF, [[_sage_const_0 , _sage_const_1 ], 
                    [_sage_const_1 , _sage_const_1 ]])
    return (a * b**(x - _sage_const_1 ))[_sage_const_0 ][_sage_const_1 ]

ans = GF(_sage_const_0 )
x = _sage_const_10 **_sage_const_14 
for i in (ellipsis_range(_sage_const_1  ,Ellipsis, _sage_const_10 **_sage_const_5 )) :
    x = next_prime(x)
    ans += fib(x)
    print i, x, ans
print ans