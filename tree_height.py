# python3

import sys
import threading
#import numpy as np

def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    for i in range(n):
        j = i
        curr = 1
        while(parents[j]!=-1):
            curr = curr+1
            j = parents[j]
        height = curr
        if curr>height:
            max_heigth=curr
        else:
            max_height=height
    return max_height + 1
    pass

def main():
    # implement input form keyboard and from files
    txt = input()
    if 'I' in txt:
        nodes = int(input())
        arr = input()
        parents = map(int,arr.split())
        parents = list(parents)
        print(compute_height(nodes, parents))
    if 'F' in txt:
        path = input()
        if '.a' not in path:
            with open(path,'r') as file:
                nodes = int(file.readline())
                data = file.read()
                parents = map(int,data.split())
                parents = list(parents)
                print(nodes)
                print(parents)
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
