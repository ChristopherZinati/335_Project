# Program with visualization of sorting algorithms
# Implements Bubble, Merge and Quick Sort in Python
# Authors: Victor Vu, Christopher Zinati, Noah Yarbrough
# Group: Syntax Sages 

import matplotlib.pyplot as plot # required library for plot
import numpy as np # contains object to manipulate plot
import time # required library to count runtime of each algorithm
from matplotlib.widgets import Button # imports buttons
from matplotlib.widgets import Button, RadioButtons # import selection menu
from numpy import random # needed to use randomly generated lists

# Quick Sort Function
def quick_sort(L, graph, start = 0, end = None): # comparison to pivot point by spliting list
    start_time = time.time
    if end is None:
        end = len(L) - 1
    if start >= end:
        return

    pivot = L[end]
    i = start

    for j in range(start, end):
        if L[j] < pivot:
            L[i], L[j] = L[j], L[i]
            i += 1

            # Gui Portion
            graph.clear() # reset for next execution
            graph.set_title('Quick Sort')
            graph.bar(np.arange(len(L)), L, align='center') # set type to bar graph
            graph.set_xticks(np.arange(len(L))) # set axis positions
            graph.set_xticklabels(L) # then label axis using array elements
            plot.pause(0.5) # delay updating to visualize sorting

    L[i], L[end] = L[end], L[i]

    quick_sort(L, graph, start, i - 1)
    quick_sort(L, graph, i + 1, end)

def run_quick_sort(L, graph):
    start_time = time.time()
    quick_sort(L, graph)
    end_time = time.time()
    runtimeSeconds = end_time - start_time
    runtimeMS = runtimeSeconds*1000000
    print('Quick Sort', runtimeMS)
    
# Merge Sort Function                 
def merge_sort(L, graph, le, ri):
    if le < ri:
        mid = (le + ri) // 2
        merge_sort(L, graph, le, mid)
        merge_sort(L, graph, mid + 1, ri)
        merge(L, graph, le, mid, ri)

def merge(L, graph, le, mid, ri):
    left_arr = L[le:mid + 1].copy()
    right_arr = L[mid + 1:ri + 1].copy()

    i = j = 0
    k = le

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            L[k] = left_arr[i]
            i += 1
        else:
            L[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        L[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        L[k] = right_arr[j]
        j += 1
        k += 1

    # Clear and redraw the entire bar graph
    graph.clear() # reset for next execution
    graph.set_title('Merge Sort')
    graph.bar(np.arange(len(L)), L, align='center') # set type to bar graph
    graph.set_xticks(np.arange(len(L))) # set axis positions
    graph.set_xticklabels(L) # then label axis using array elements
    plot.pause(0.5) # delay updating to visualize sorting

    while paused: # check for pause condition
                        plot.pause(0.1) # in .1 seconds stop

# Bubble Sort Function
def bubble_sort(L, graph): # pass in list/graph 
    start_time = time.time() 
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
    runtimeSeconds = end_time - start_time
    runtimeMS = runtimeSeconds*1000000
    print('Bubble Sort', runtimeMS)



# L = [27, 14, 56, 8, 39, 73, 22, 61] # global list of numbers
L = [random.randint(1, 100) for _ in range(5, 15)] # randomly generated list
sorting_method = 'Bubble Sort' # default sorting method
L2 = L # store a copy of the initial list

# Handle selection of sorting method
def choose_sorting_method(label):
    global sorting_method
    sorting_method = label

# Call to start to sorting
def start(event): # wait on the event button clicked
    global L, sorting_method
    start_button.set_active(False) # prevents starting twice
    start_button.ax.figure.canvas.draw() # update button
    if sorting_method == 'Bubble Sort':
        bubble_sort(L, graph)
    elif sorting_method == 'Merge Sort':
        merge_sort(L, graph, 0, len(L) - 1)
    elif sorting_method == 'Quick Sort':
        run_quick_sort(L, graph)

# Stop all sorting
def stop(event):
    global paused # access global variable
    paused = not paused # toggle the state
    pause_button.label.set_text('Resume' if paused else 'Pause') # switch text

def clear(event):
    global L, L2, paused, sorting_method
    start_button.set_active(True)  # reactivate start
    L = L2[:] # reset L to its original unsorted copy
    graph.clear() # clear the graph
    # replot the original graph
    L = [random.randint(1, 100) for _ in range(5, 15)] # generate a brand new list
    graph.set_title('Select a Sorting Method')
    graph.bar(np.arange(len(L)), L, align='center')  
    graph.set_xticks(np.arange(len(L)))
    graph.set_xticklabels(L)
    if paused: # ensure program is not paused
        paused = False
        pause_button.label.set_text('Pause')
    plot.draw()  # redraw the plot
    if sorting_method == 'Bubble Sort':
        bubble_sort(L, graph)  # re-sort the initial list
    elif sorting_method == 'Merge Sort':
        merge_sort(L, graph, 0, len(L) - 1)
    elif sorting_method == 'Quick Sort':
        run_quick_sort(L, graph)

# Initial list
def draw_initial_list(L):
    graph.clear()
    graph.set_title('Select a Sorting Method')
    graph.bar(np.arange(len(L)), L, align='center')
    graph.set_xticks(np.arange(len(L)))
    graph.set_xticklabels(L)

# Create a figure and axis for the plot
fig, graph = plot.subplots()
draw_initial_list(L)

# Selection button sorting method
sorting_buttons_ax = fig.add_axes([0.125, 0.88, 0.2, 0.121]) # (Left/Right, Up/Down, Width, Height)
sorting_buttons = RadioButtons(sorting_buttons_ax, ('Bubble Sort', 'Merge Sort', 'Quick Sort'))
sorting_buttons.on_clicked(choose_sorting_method)

# Start Button
graph_button = fig.add_axes([0.8, 0.01, 0.1, 0.05]) # button positions
start_button = Button(graph_button, 'Start', color='#90EE90')
start_button.on_clicked(start)

# Pause Button
paused = False # not yet paused
graph_button = fig.add_axes([0.7, 0.01, 0.1, 0.05]) 
pause_button = Button(graph_button, 'Pause')
pause_button.on_clicked(stop)

# Reset Button
graph_button = fig.add_axes([0.6, 0.01, 0.1, 0.05]) 
reset_button = Button(graph_button, 'Reset')
reset_button.on_clicked(clear)

plot.show() # output