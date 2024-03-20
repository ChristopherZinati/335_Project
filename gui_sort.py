"""*******************************************************************************  
   Author Information:
   Name: Victor V. Vu
   Email: vuvictor@csu.fullerton.edu

   Major Contributors: Christopher Zinati and Noah Yarbrough

   Program Information:
   This File: gui_sort.py   
   Description: Program with visualization of sorting algorithms. 
   Implements Bubble, Merge and Quick Sort in Python.

   Copyright (C) 2024 Victor V. Vu, Christopher Zinati and Noah Yarbrough
   This program is free software: you can redistribute it and/or modify it under
   the terms of the GNU General Public License version 3 as published by the
   Free Software Foundation. This program is distributed in the hope that it
   will be useful, but WITHOUT ANY WARRANTY without even the implied Warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
   Public License for more details. A copy of the GNU General Public License v3
   is available here: <https://www.gnu.org/licenses/>.
*******************************************************************************"""

import matplotlib.pyplot as plot # required library for plot
import numpy as np # contains object to manipulate plot
import time # required library to count runtime of each algorithm
from matplotlib.widgets import Button # imports buttons
from matplotlib.widgets import RadioButtons # import selection menu
from numpy import random # needed to use randomly generated array

# Quick Sort Function
def quick_sort(L, graph, start = 0, end = None): # start at the first element and end at the last
    if end is None: # check if the last element is not specified 
        end = len(L) - 1 # set it to the last index of list 'L'
    if start >= end: # if start index is greater, end the function
        return

    # Select pivot and determine start/end indexes
    pivot = L[end] 
    i = start 
    j = end - 1 # subtract as pivot is the last element

    # Split list and compare until l/r meet 
    while i <= j:
        while L[i] < pivot: # if the current element is less than the pivot
            i += 1 # increment index
        while L[j] > pivot:
            j -= 1 # de-increment j
        if i <= j: # ensure loops continues swapping until i and j meeet
            L[i], L[j] = L[j], L[i] # swap current element positions
            i += 1 # move cursor right 
            j -= 1 # move cursor left

    graph.clear() # reset for next execution
    graph.set_title('Quick Sort') # titled plot
    graph.bar(np.arange(len(L)), L, align='center') # set type to bar graph
    graph.set_xticks(np.arange(len(L))) # set axis positions
    
    if L is not None: # if L exists
        graph.set_xticklabels(L) # update axis label

    plot.pause(0.5) # update every .5 seconds 
    while paused: # check for pause condition
        plot.pause(0.1) # in .1 seconds, pause

    L[i], L[end] = L[end], L[i] # swap the pivot with element at index i
    # Recursive calls for the sublists before and after the pivot
    quick_sort(L, graph, start, i - 1)
    quick_sort(L, graph, i + 1, end)
    plot.draw() # redraw to update plot

# Function to run the quick_sort algorithm with timing
def run_quick_sort(L, graph):
    graph.clear() # redraw to update plot  
    start_time = time.time() # record starting time
    quick_sort(L, graph) # call quick_sort function
    end_time = time.time() # record ending time
    runtimeSeconds = end_time - start_time # calculate runtime in seconds
    runtimeMS = runtimeSeconds * 1000000 # convert runtime to microseconds
    print('Quick Sort:', runtimeMS, 'microseconds')  

    # Gui portion
    graph.clear() # update graph 
    graph.set_title('Quick Sort') # set title
    graph.bar(np.arange(len(L)), L, align='center') # set graph to bar
    graph.set_xticks(np.arange(len(L))) # set axis size
    graph.set_xticklabels(L) # label axis

# Merge Sort Function  
def merger(L, graph, le, ri):
    start_time = time.time() # start timer
    def merge_sort(L, graph, le, ri): # nested merger, prevents resetting timer
        if le < ri: # if left less than right side
            mid = (le + ri) // 2 # split array
            # Recursion function calls
            merge_sort(L, graph, le, mid)
            merge_sort(L, graph, mid + 1, ri)
            merge(L, graph, le, mid, ri) # helper function

    # Helper function for merge sort
    def merge(L, graph, le, mid, ri):
        # Store copies for array
        left_arr = L[le:mid + 1].copy()
        right_arr = L[mid + 1:ri + 1].copy()

        i = j = 0 # start cursor at 0
        k = le # main array

        # If elements remain, continue loop
        while i < len(left_arr) and j < len(right_arr): # while sides are not completed
            if left_arr[i] <= right_arr[j]: # if one side is less than/equal
                L[k] = left_arr[i] # swap the out the larger number
                i += 1 # advance to the next element
            else:
                L[k] = right_arr[j]
                j += 1
            k += 1 # advance the main array

        # Handle case of odd numerbed array
        while i < len(left_arr):
            L[k] = left_arr[i] # add left over elements into array
            i += 1 # move the pointer
            k += 1 # main array must advance
        while j < len(right_arr):
            L[k] = right_arr[j]
            j += 1
            k += 1
 
        # Gui portion
        graph.clear() 
        graph.set_title('Merge Sort') 
        graph.bar(np.arange(len(L)), L, align='center') 
        graph.set_xticks(np.arange(len(L))) 
        graph.set_xticklabels(L) 
        plot.pause(0.5) # update in .5 seconds to visualize sorting

        while paused: # check for pause condition
            plot.pause(0.1) # in .1 seconds stop

    merge_sort(L, graph, le, ri) # call merger
    end_time = time.time() # end timer
    runtimeSeconds = end_time - start_time # compute total runtime
    runtimeMS = runtimeSeconds*1000000 # convert to microseconds
    print('Merge Sort:', runtimeMS, 'microseconds') 

# Bubble Sort Function
def bubble_sort(L, graph): # pass in list/graph 
    start_time = time.time() 
    n = len(L) # find the length of l and store in n
    for i in range(n): # ensure number of passes does not exceed length 
        for j in range(0, n-i-1): # start at 1st element but end before the largest last element 
                if L[j] > L[j+1]: # if element is greater than the next element 
                    L[j], L[j+1] = L[j+1], L[j] # swap positions

                    # Timer calculation
                    end_time = time.time()
                    runtimeSeconds = end_time - start_time
                    runtimeMS = runtimeSeconds*1000000 

                    # Gui Portion
                    graph.clear() 
                    graph.set_title('Bubble Sort')
                    graph.bar(np.arange(len(L)), L, align='center') 
                    graph.set_xticks(np.arange(len(L))) 
                    graph.set_xticklabels(L) 
                    plot.pause(0.5) 

                    while paused: # pause function
                        plot.pause(0.1) 

    print('Bubble Sort: ', runtimeMS, 'microseconds') 

L = [27, 14, 56, 8, 39, 73, 22, 61] # initial list of numbers
sorting_method = 'Bubble Sort' # default sorting method
paused = False # start not yet paused

# Handle selection of sorting method
def choose_sorting_method(label):
    global sorting_method # access global variable
    sorting_method = label # set to selection

# Call to start to sorting selected function
def start(event): # wait on the event button clicked
    global L, sorting_method
    start_button.set_active(False) # prevents starting twice
    if sorting_method == 'Bubble Sort':
        bubble_sort(L, graph)
    elif sorting_method == 'Merge Sort':
        merger(L, graph, 0, len(L) - 1)
    elif sorting_method == 'Quick Sort':
        run_quick_sort(L, graph)

# Stop all sorting
def stop(event):
    global paused 
    paused = not paused # toggle the state
    pause_button.label.set_text('Resume' if paused else 'Pause') # switch text

# Clear the graph and generate random array
def clear(event):
    global L, paused, sorting_method
    graph.clear() 
    #L = [42, 12, 45, 23, 87, 32, 11, 24, 22, 50, 62, 71] # Left in code for using a fixed list
    L = [random.randint(1, 100) for _ in range(5, 15)] # generate a new random list
    # Reset gui
    graph.bar(np.arange(len(L)), L, align='center')  
    graph.set_xticks(np.arange(len(L)))
    graph.set_xticklabels(L)

    # Ensure program is not paused
    if not paused: # re-sort the initial lists
        if sorting_method == 'Bubble Sort':
            bubble_sort(L, graph) 
        elif sorting_method == 'Merge Sort':
            merger(L, graph, 0, len(L) - 1)
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
graph_button = fig.add_axes([0.7, 0.01, 0.1, 0.05]) 
pause_button = Button(graph_button, 'Pause')
pause_button.on_clicked(stop)

# Reset Button
graph_button = fig.add_axes([0.6, 0.01, 0.1, 0.05]) 
reset_button = Button(graph_button, 'Reset')
reset_button.on_clicked(clear)

plot.show() # output graph
