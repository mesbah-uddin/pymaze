# foo.py
print(__name__, ": '__main__' for entry-point, 'foo' otherwise")

import math

def fun():
    return("called foo.fun()")

print("**** foo : (unguarded) executed always")
if __name__ == "__main__":
    print(">>>> foo : (main-guarded) executed for entry-point and not with import; " + fun())
    print(">>>> foo : (main-guarded) executed for entry-point and not with import; pi=" + str(math.pi))
print("**** foo : (unguarded) executed always")
