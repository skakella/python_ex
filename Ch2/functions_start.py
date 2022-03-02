#
# Example file for working with functions
#

# define a basic function

def fun1():
    print("I am a function1")
# function that takes arguments
def fun2(arg1, arg2):
    print(arg1, " " , arg2)

# function that returns a value

def cube(arg1):
    return arg1*arg1*arg1

# function with default value for an argument
def power(num,x=1):
    r = 1
    for x in range(x):
        r = r*num
    return r

#function with variable number of arguments
def multi_arg(*args):
    # result = 0
    # for x in args:
    #     result = result + x
    return args[3]

money = 2000

def add_money():
    global money
    money = money + 1

print(money)
add_money()
print(money)   


# fun1()
# print(fun1())
# print(fun1)
# fun2(10,20)
# print(fun2(5,6))
# print(cube(5))
# print(power(2))
# print(power(3,4))
# print(power(x=5,num=2))
# print(multi_arg(5))
# print(multi_arg(5,6))
# print(multi_arg(5,6.7,8))
