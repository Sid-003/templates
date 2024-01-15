from itertools import accumulate
from functools import reduce


def rabin_karp(t, s, p=31, m=10**9 + 9):
    """
    Return all occurences of s in t.

    Reference Used: https://cp-algorithms.com/string/rabin-karp.html
    """
    T = len(t)
    S = len(s)

    pow = list(accumulate(range(max(S, T)-1),
               lambda a, x: (a * p) % m, initial=1))

    def hash_accum(a, x): return (a + (ord(x[1]) - 97 + 1) * pow[x[0]]) % m
    hash = list(accumulate(enumerate(t), hash_accum, initial=0))
    phash = reduce(hash_accum, enumerate(s), 0)

    return (i for i in range(T-S+1) if ((hash[i+S]-hash[i]+m) % m) == ((phash * pow[i]) % m))

