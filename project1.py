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
    print('Merge Sort', runtimeMS)
                    
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
    start_time = time.time() # measure time taken
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
                    plot.pause(0.5) # delay updating to visualize sorting

                    while paused: # check for pause condition
                        plot.pause(0.1) # in .1 seconds stop
    end_time = time.time()
    runtimeSeconds = start_time - end_time
    runtimeMS = runtimeSeconds*1000000
    print('Bubble Sort', runtimeMS)

L = [27, 14, 56, 8, 39, 73, 22, 61, 5, 48] # Global list of numbers

# Call to start to sorting
def start(event): # wait on the event button clicked
    global L # access the values
    bubble_sort(L, graph) # call bubble sort
    # merge_sort_visuals(L, graph) # call merge sort (Commented out for now will be creating selection menu instead)

# Stop all sorting
def stop(event):
    global paused # access global variable
    paused = not paused # toggle the state
    if paused:
        start_button.set_active(False) # ensures start button cannot sort
    elif not paused:
        start_button.set_active(True) # else reverse it
    pause_button.label.set_text('Resume' if paused else 'Pause') # switch text

# Initial list
def draw_initial_list(L):
    graph.clear()
    graph.set_title('Please Select Sorting Method')
    graph.bar(np.arange(len(L)), L, align='center')
    graph.set_xticks(np.arange(len(L)))
    graph.set_xticklabels(L)

# Create a figure and axis for the plot
fig, graph = plot.subplots()
draw_initial_list(L)

# Start Button
graph_button = fig.add_axes([0.8, 0.01, 0.1, 0.05]) # button positions
start_button = Button(graph_button, 'Start')
start_button.on_clicked(start)

# Pause Button
paused = False # not yet paused
graph_button = fig.add_axes([0.7, 0.01, 0.1, 0.05]) 
pause_button = Button(graph_button, 'Pause')
pause_button.on_clicked(stop)

# Reset Button
#graph_button = fig.add_axes([0.6, 0.01, 0.1, 0.05]) 
#reset_button = Button(graph_button, 'Reset')
#reset_button.on_clicked(draw_initial_list)

plot.show() # output


