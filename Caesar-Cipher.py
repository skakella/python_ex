#!/usr/bin/env python3

def cipher(str,places=0):
    orig_str=list(str.encode('ascii'))
    #return orig_str
    ciphter_str=""
    for n in orig_str:
        ciphter_str = ciphter_str+chr((n+places))
    return ciphter_str

input_string = input("Enter a string: ").strip()
input_places=int(input("Enter a number for places: "))
#print(chr(ord(input_string[0])+input_places))
print(cipher(input_string,input_places))
