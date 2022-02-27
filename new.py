import timeit

def ispalindrom(string):

    left = iter(string)
    right = iter(string[::-1])

    i = 0

    str_len = len(string)

    while i < str_len/2:
        if next(left) != next(right):
            print("Not Palindrom")
            return False
        i = i + 1
        
    
    print("palindrom")
    return True


ispalindrom("suresh")
