
def is_sorted(li):
    
    for g in li:
        if list(g) != sorted(g):            
            return False
    return True


#grid = np.array([[abc],[def],[ghi]])
grid = ['eabcd','fghij','olkmn','trpqs','xywuv']

    sorted_grid =[]

    for g in grid:
        sorted_grid.append(sorted(g))
        

    column_grid = []

    for c in range(len(sorted_grid)):
        column_string = ""
        for g in sorted_grid:
            column_string = column_string+g[c]
        column_grid.append(column_string)

    column_sorted = is_sorted(column_grid)

    print(sorted_grid)
    if  column_sorted:
        print("YES")    
    else:
        print("NO")




