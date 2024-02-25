# Program with visualization of sorting algorithms
# Implements Bubble, Merge and Quick Sort in Python
# Authors: Victor Vu, 
# Group: Syntax Sages 

import matplotlib.pyplot as plot # required library for plot
import numpy as np # contains object to manipulate plot
from matplotlib.widgets import Button # imports buttons

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
                    plot.pause(0.5) # delay updating to visualize sorting

                    while paused: # check for pause condition
                        plot.pause(0.1) # in .1 seconds stop

L = [27, 14, 56, 8, 39, 73, 22, 61, 5, 48] # Global list of numbers

# Call to start to sorting
def start(event): # wait on the event button clicked
    global L # access the values
    bubble_sort(L, graph) # call bubble sort

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



