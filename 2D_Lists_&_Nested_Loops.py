#2D Lists:

# All the elements in number_grid list will be lists
# We are creating a grid with four rows with three collumns
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#How to access individual elements of this grid:
#print(number_grid[0][2]) #where [row][collumn]


#Nested Loop:

for row in number_grid:
    #print(row)
    for col in row:
        print(col)