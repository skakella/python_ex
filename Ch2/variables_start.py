


# Global vs. local variables in functions


f=0
def myfun():
    global f
    f="Zero"
    print(f)

myfun()
print(f)
del f
print(f)