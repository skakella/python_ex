import numpy as np
import sys

if __name__ == '__main__':

    # dtype = [('name','S10'),('age',int),('height',float)]
    # data = [('Suresh',40,5.7),('Pandu',34,5.2),('Abhi',4,3.3),('Aki',10,4.7)]

    # family = np.array(data,dtype=dtype)

    # print(family)

    # print(np.sort(family,order='age'))

    # print(family)
    

    li = [2,3,8,4,5]
    8+10+8+11+32
    li.sort(reverse=True)
    
    result = sum( [ pow(2,i)*li[i] for i in range(len(li)) ])
    print(result)