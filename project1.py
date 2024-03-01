# Program with visualization of sorting algorithms
# Implements Bubble, Merge and Quick Sort in Python
# Authors: Victor Vu, Christopher Zinati, Noah Yarbrough
# Group: Syntax Sages 

import matplotlib.pyplot as plot # required library for plot
import numpy as np # contains object to manipulate plot
import time # required library to count runtime of each algorithm
from matplotlib.widgets import Button # imports buttons
from matplotlib.widgets import RadioButtons # import selection menu
from numpy import random # needed to use randomly generated lists

# Quick Sort Function
def quick_sort(L, graph, start = 0, end = None): # comparison to pivot point by spliting list
    if end is None: # check if the variable 'end' is None
        end = len(L) - 1 # set it to the last index of list 'L'
    if start >= end: # if the 'start' index is greater than or equal to the 'end' index
        return

    # Select the pivot element, which is the last element of the list
    pivot = L[end]
    i = start # 'i' to the starting index
    j = end - 1 # j is ending index

    # While i has not reached the last index
    while i <= j:
        while L[i] < pivot: # check if the current element is less than the pivot
            i += 1 # increment index
        while L[j] > pivot:
            j -= 1 # deincrement j
        if i <= j: # Swap the current element with the element at index 'i'
            L[i], L[j] = L[j], L[i]
            i += 1
            j -= 1
    # Gui portion - see merge sort 
    graph.clear()
    graph.set_title('Quick Sort')
    graph.bar(np.arange(len(L)), L, align='center')
    graph.set_xticks(np.arange(len(L)))
    if L is not None:
        graph.set_xticklabels(L) # update axis label

    plot.pause(0.5) # in .5 seconds update
    while paused: # check for pause condition
        plot.pause(0.1)

     # Swap the pivot element with the element at index 'i'
    L[i], L[end] = L[end], L[i]

    # recursive calls quick_sort for the sublists before and after the pivot
    quick_sort(L, graph, start, i - 1)
    quick_sort(L, graph, i + 1, end)

    # Function to run the quick_sort algorithm with timing
def run_quick_sort(L, graph):
    graph.clear()
    # Record the starting time
    start_time = time.time()
    # Call quick_sort function
    quick_sort(L, graph)
    # Record the ending time
    end_time = time.time()
    # Calculate the runtime in seconds
    runtimeSeconds = end_time - start_time
    # Convert runtime to microseconds
    runtimeMS = runtimeSeconds * 1000000
    # Print the runtime of the quick sort algorithm
    print('Quick Sort:', runtimeMS, 'microseconds')    

# Merge Sort Function  
def merger(L, graph, le, ri):
    start_time = time.time() # start timer
    def merge_sort(L, graph, le, ri): # nested merger, prevent resetting timer
        if le < ri: # condition: left is less than right
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

        # If elements remain, contine the loop
        while i < len(left_arr) and j < len(right_arr):
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
 
        # Clear and redraw the entire bar graph
        graph.clear() # reset for next execution
        graph.set_title('Merge Sort') # titled plot
        graph.bar(np.arange(len(L)), L, align='center') # set type to bar graph
        graph.set_xticks(np.arange(len(L))) # set axis positions
        graph.set_xticklabels(L) # then label axis using array elements
        plot.pause(0.5) # delay updating to visualize sorting

        while paused: # check for pause condition
            plot.pause(0.1) # in .1 seconds stop

    merge_sort(L, graph, le, ri) # call merger
    end_time = time.time() # end timer
    runtimeSeconds = end_time - start_time # compute total runtime
    runtimeMS = runtimeSeconds*1000000 # convert to microseconds
    print('Merge Sort:', runtimeMS, 'microseconds') # print

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

    print('Bubble Sort: ', runtimeMS, 'microseconds') # check runtime

L = [27, 14, 56, 8, 39, 73, 22, 61] # global list of numbers
#L = [random.randint(1, 100) for _ in range(5, 15)] # randomly generated list
sorting_method = 'Bubble Sort' # default sorting method
paused = False # start not yet paused

# Handle selection of sorting method
def choose_sorting_method(label):
    global sorting_method
    sorting_method = label

# Call to start to sorting
def start(event): # wait on the event button clicked
    global L, sorting_method
    start_button.color = None # indicates button is off
    start_button.set_active(False) # prevents starting twice
    start_button.ax.figure.canvas.draw() # update button
    if sorting_method == 'Bubble Sort':
        bubble_sort(L, graph)
    elif sorting_method == 'Merge Sort':
        merger(L, graph, 0, len(L) - 1)
    elif sorting_method == 'Quick Sort':
        run_quick_sort(L, graph)

# Stop all sorting
def stop(event):
    global paused # access global variable
    paused = not paused # toggle the state
    pause_button.label.set_text('Resume' if paused else 'Pause') # switch text

# Clear the graph and generate random array
def clear(event):
    global L, paused, sorting_method
    graph.clear() # clear the graph
    L = [42, 12, 45, 23, 87, 32, 11, 24, 22, 50, 62, 71]
    #L = [random.randint(1, 100) for _ in range(5, 15)] # generate a brand new list
    graph.set_title('Select a Sorting Method')
    graph.bar(np.arange(len(L)), L, align='center')  
    graph.set_xticks(np.arange(len(L)))
    graph.set_xticklabels(L)

    # Reactivate start button
    plot.draw() # redraw the plot
    if not paused: # ensure program is not paused
        if sorting_method == 'Bubble Sort':
            bubble_sort(L, graph)  # re-sort the initial list
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

plot.show() # output