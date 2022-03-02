#
# Example file for working with conditional statements
#


def main():
    x, y = 100, 100

    # conditional flow uses if, elif, else
    if (x > y):
        result = " X is greater than Y"
    elif (x < y):
        result = " X is smaller than Y"
    else:
        result = " X is same as Y"
    
    print(result)

    # conditional statements let you use "a if C else b"

    r = "X is same as Y" if ( x == y ) else "X is not same as Y"
    print(r)

if __name__ == "__main__":
    main()
