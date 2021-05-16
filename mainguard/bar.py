# bar.py
print(__name__, ": '__main__' for entry-point, 'bar' otherwise")

print("bar : begin import")
import foo
print("bar : end import")

if __name__ == "__main__":
    print("bar : (main-guarded) executed for entry-point and not with import; " + foo.fun())
