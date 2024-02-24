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
                    plot.pause(1.0) # delay updating to visualize sorting

# Call to start to sorting
def start(event): # wait on the event button clicked
    L = [2, 4, 1, 8, 3, 6] # list input
    bubble_sort(L, graph) # call bubble sort

# Create a figure and axis for the plot
fig, graph = plot.subplots()

# Start Button
graph_button = fig.add_axes([0.8, 0.01, 0.1, 0.05]) # button positions
start_button = Button(graph_button, 'Start')
start_button.on_clicked(start)
plot.show() # output


