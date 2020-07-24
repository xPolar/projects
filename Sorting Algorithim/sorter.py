def sort(array): # Function to sort a list from lest to greatest
    length = len(array) # Gets the length of your list
    for i in range(length): # Goes through a for loop for the length of your list
        sorted = True # Declares a value called sorted to False, will be used later
        for x  in range(length - i - 1): # Compares the current item and adjacent item
            if array[x] > array[x + 1]: # Checks to see if the current item is the same as the adjacent item
                array[x], array[x + 1] = array[x + 1], array [x] # Swaps the items
                sorted = False # Sets sorted to False to continue the for loop
        if sorted == True: # Checks to see if the list has been fully sorted yet
            break # Stops the for loops
    return array # Returns the list to be used
print(sort([1, 534534, 335, 53 , 235 ,25235 , 325, 13, 234, 6345, 457, 1234, 234, 54, 76, 8, 65, 5, 253, 54, 6, 56]))