# Program with visualization of sorting algorithms
# Implements Bubble, Merge and Quick Sort in Python
# Authors: Victor Vu, Christopher Zinati,
# Group: Syntax Sages 

import time # required library to count runtime of each algorithm
import matplotlib.pyplot as plot # required library for plot
import numpy as np # contains object to manipulate plot
from matplotlib.widgets import Button # imports buttons

# Merge Sort Function
def merge_sort_time(L):
    start_time = time.time()
    # merge sort is nested within time function in order to not 
    # reset the timer when recursively called
    def merge_sort(L):
            if len(L) > 1:
                mid = len(L)//2 # find midpoint
                le = L[:mid] # divide into left and right subarrays
                ri = L[mid:] 
                merge_sort[le] # recursively sort both halves
                merge_sort[ri]

                i = j = k = 0
                while i < len(le) and j < len(ri):
                    if le[i] < ri[j]:
                        L[k] = le[i]
                        i += 1
                    else:
                        L[k] = ri[j]
                        j += 1
                    k += 1
                while i < len(le):
                    L[k] = le[i]
                    i += 1
                    k += 1

                while j < len(ri):
                    j += 1
                    k += 1
            return L
     
    end_time = time.time()
    runtimeSeconds = start_time - end_time
    runtimeMS = runtimeSeconds*1000000
    return runtimeMS
                    
def merge_sort_visuals(L, graph): # pass in list/graph 
    if len(L) > 1:
        mid = len(L)//2 # find midpoint
        le = L[:mid] # divide into left and right subarrays
        ri = L[mid:] 
        merge_sort_visuals(le, graph) # recursively sort both halves
        merge_sort_visuals(ri, graph)
        i = j = k = 0
        while i < len(le) and j < len(ri):
            if le[i] < ri[j]:
                L[k] = le[i]
                i += 1
            else:
                L[k] = ri[j]
                j += 1
            k += 1
        while i < len(le): # if one half becomes exhausted before the other
            L[k] = le[i]
            i += 1
            k += 1
        while j < len(ri):
            L[k] = ri[j]
            j += 1
            k += 1
  
    # gui portion (explanation in bubble_sort) 
    graph.clear()
    graph.set_title('Merge Sort')
    graph.bar(np.arange(len(L)), (L), align='center')
    graph.set_xticks(np.arange(len(L)))
    graph.set_xticklabels(L)
    plot.pause(1.0)
    return L, graph   

# Bubble Sort Function
def bubble_sort(L, graph): # pass in list/graph 
    n = len(L) # find the length of l and store in n
    for i in range(n): # ensure number of passes does not exceed length 
        for j in range(0, n-i-1): # start at 1st element but end before the largest last element 
                if L[j] > L[j+1]: # if element is greater than the next element 
                    L[j], L[j+1] = L[j+1], L[j] # swap positions 

                    # Gui Portion
                    graph.clear() # reset for next execution
                    graph.set_title('Bubble Sort')
                    graph.bar(np.arange(len(L)), L, align='center') # set type to bar graph
                    graph.set_xticks(np.arange(len(L))) # set axis positions
                    graph.set_xticklabels(L) # then label axis using array elements
                    plot.pause(1.0) # delay updating to visualize sorting

# Call to start to sorting
def start(event): # wait on the event button clicked
    L = [2, 4, 1, 8, 3, 6] # list input
    bubble_sort(L, graph) # call bubble sort
    merge_sort_visuals(L, graph) # call merge sort

# Create a figure and axis for the plot
fig, graph = plot.subplots()

# Start Button
graph_button = fig.add_axes([0.8, 0.01, 0.1, 0.05]) # button positions
start_button = Button(graph_button, 'Start')
start_button.on_clicked(start)
plot.show() # output


