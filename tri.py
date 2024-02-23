## Import Block ##
import numpy as np
import warnings as warnings

## Inputs Block ##
size_triangle = int(input("Give An Integer Row Number for the Triangle: ")) # This already does the error handling for you for the int issue will not just blindly convert data
dir_triangle = input("Give Direction of the Triangle (^ for up, v for down, < for left, or > for right): ")

## Warnings Block ##
if not(dir_triangle in [">", "<", "^", "v"]):
    warnings.warn("The direction of the triangle is not a reasonable direction")
                  
if size_triangle < 0:
    warnings.warn("The triangle size needs to be positive")

## Layout of Triangle Queue ##                
if (dir_triangle == ">") or (dir_triangle == "<"):
    triangle_queue=np.zeros((size_triangle+(size_triangle-1), size_triangle))

    if dir_triangle == ">":
    #The Right Facing Triangle Queue Block
        for n in range(size_triangle):
            #row,column
            if n == 0:
                triangle_queue[size_triangle-1,size_triangle-1] = 1
            else:
                check = np.nonzero(triangle_queue[:,-n]==1)
                
                position_increase = check[0]+1
                position_decrease = check[0]-1

                # It was needing the loop because you were doing a weird slice indexing... you specify by [r,c] not [r] [c] once you change to [r,c] you can do it this way
                triangle_queue[np.unique(np.hstack((position_increase, position_decrease))),(size_triangle-1)-n] = 1
                                   
    elif dir_triangle == "<":
    #The Left Facing Triangle Queue Block
        for n in range(size_triangle):
            if n == 0: 
                triangle_queue[size_triangle-1,n] = 1
            else:
                check = np.nonzero(triangle_queue[:,n-1]==1)
                
                position_increase = check[0]+1
                position_decrease = check[0]-1
                
                # It was needing the loop because you were doing a weird slice indexing... you specify by [r,c] not [r] [c] once you change to [r,c] you can do it this way
                triangle_queue[np.unique(np.hstack((position_increase, position_decrease))),n] = 1

elif (dir_triangle == "^") or (dir_triangle == "v"): 
    triangle_queue=np.zeros((size_triangle,size_triangle+(size_triangle-1)))

    if dir_triangle == "^":
        #The Up Facing Triangle Queue Block
        for n in range(size_triangle):
            if n == 0:
                triangle_queue[n,size_triangle-1] = 1
            else:
                check = np.nonzero(triangle_queue[n-1,:]==1)
                
                position_increase = check[0]+1
                position_decrease = check[0]-1
                
                triangle_queue[n,np.unique(np.hstack((position_increase, position_decrease)))] = 1
                
    elif dir_triangle == "v":
        #The down Facing Triangle Queue Block
        for n in range(size_triangle):   
            if n == 0:
                triangle_queue[size_triangle-1,size_triangle-1] = 1
            else:
                check = np.nonzero(triangle_queue[-n,:]==1)
                
                position_increase = check[0]+1
                position_decrease = check[0]-1
                
                triangle_queue[-n-1,np.unique(np.hstack((position_increase, position_decrease)))] = 1
        
## Setting up Triangle String Array based on Triangle Queue Data ##  
triangle = np.chararray((triangle_queue.shape[0], triangle_queue.shape[1]))
triangle[triangle_queue == 0] = " "
triangle[triangle_queue == 1] = "*"

## Print Triangle -- Have to Decode because the Chararray is considered a byte array and the print will print a byte notation character ##
print(f""" {triangle.decode()}""")