

import numpy as np

if __name__ == '__main__':

    dtype = [('name','S10'),('age',int),('height',float)]
    data = [('suresh',41,5.7),('Suri',10,3.2),('Pandu',34,5.2),('Aki',10,4.7)]
    a = np.array(data,dtype=dtype)
    print(f'Array is {a}')
    
    b = a['age']
    b.sort()
    print(b)
    
    #set second as first element of the Age
    second = b[0]
    for i in range(1,len(b)):        
        if b[i] > second:
            second = b[i]
            break
   
    
    for ar in a:
        if ar['age'] == second:
            print(ar)
    
    # for i in b.sort():
    #     print(i)
    

    

