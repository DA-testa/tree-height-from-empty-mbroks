# python3

import sys
import threading
import numpy as np


def check(j, parents, height):
   
   #check tree root
    if (parents[j] == -1):
        return 1
 
    elif (height[j] != -1):
        return height[j]
    
    height[j] = check(parents[j], parents, height) + 1
    return height[j]
 

def compute_height(n, parents):
    max_height = 0
    #height_l = np.empty(n)
    height_l = np.array([-1]*(n))
 
    for j in range(n):
        max_height = max(max_height, check(j, parents, height_l))

    return max_height

def main():
    # implement input form keyboard and from files
    txt = input()
    if 'I' in txt:
        nodes = int(input())
        arr = input()
        parents = map(int,arr.split())
        parents = np.array(list(parents))
        print(compute_height(nodes, parents))
    if 'F' in txt:
        path = input()
        if '.a' not in path:
            path = "test/"+path
            with open(path,'r') as file:
                nodes = int(file.readline())
                data = file.read()
                parents = map(int,data.split())
                parents = np.array(list(parents))
                print(compute_height(nodes,parents))
        else:
             pass        
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
