#coding: latin1

from time import perf_counter as clock

infinity = float("+inf") #[]infinity

_min = min #[minmax

def min(*it: "Iterable<T>", **kw: "ifempty with value") -> "T":
    try:
        return _min(*it)
    except ValueError:
        if 'ifempty' in kw: return kw['ifempty']
        raise ValueError

_max = max

def max(*it: "Iterable<T>", **kw: "ifempty with value") -> "T":
    try:
        return _max(*it)
    except ValueError:
        if 'ifempty' in kw: return kw['ifempty'] 
        raise ValueError #]minmax

def argmin(iterable: "Iterable<T>", fn: "T -> S", ifempty: "T or None"=None) -> "T": #[arg
    try: 
        return _min( (fn(x), x) for x in iterable )[1]
    except ValueError:
        return ifempty

def argmax(iterable: "Iterable<T>", fn: "T -> S", ifempty: "T or None"=None) -> "T":
    try: 
        return _max( (fn(x), x) for x in iterable )[1]
    except ValueError:
        return ifempty #]arg

def count(iterable: "Iterable<T>") -> "int": #[count
    return len(iterable) if hasattr(iterable, "__len__") else sum(1 for _ in iterable) #]count 

def chronometer(tmin: "float", method: "function", *parameters) -> "float": #[chrono
    t1 = t2 = clock()
    r = 0
    while t2 - t1 < tmin:
        method(*parameters)
        t2 = clock()
        r += 1
    t3 = t4 = clock()
    aux = 0
    while aux < r:
        t4 - t3
        t4 = clock()
        aux += 1
    return ((t2 - t1) - (t4 - t3)) / r #]chrono
