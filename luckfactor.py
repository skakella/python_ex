import numpy as np

def luckBalance(k, contests):
    # Write your code here
    
    # temp_array = np.array([ [8 ,1], [9, 1], [10, 0],[7,1]])
    # print(np.sort(temp_array,axis=0)
    pass 


    


    

#first_multiple_input = input().rstrip().split()

# n = int(first_multiple_input[0])

# k = int(first_multiple_input[1])

# contests = []

# for _ in range(n):
#     contests.append(list(map(int, input().rstrip().split())))

# result = luckBalance(k, contests)
#luckBalance(1,1)
k = 3
contests = np.array([[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]])
sorted_contests = np.sort(contests,axis=0)
total_import_contests = sum([ a[1]  for a in contests if a[1] == 1 ])
print(total_import_contests)



