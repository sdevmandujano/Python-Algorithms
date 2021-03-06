def binary_search(list, item):
  # low and high keep track of which part of the list you'll search in.

  low = 0 # first item of the list 
  high = len(list) - 1 #last item of the list 

  # While you haven't narrowed it down to one element ...
  while low <= high:
    # ... check the middle element
    mid = (low + high) // 2   #two slashes mean integer division is gonna get the answer without remained 
    guess = list[mid] # middle element of the list 
    # Found the item.
    if guess == item:
      return mid
    # The guess was too high.
    if guess > item:
      high = mid - 1 # cuts half of the top of the array 
    # The guess was too low.
    else:
      low = mid + 1 #cuts half of the bottom of the array 

  # Item doesn't exist
  return None

my_list = [1, 3, 5, 7, 9]
print (binary_search(my_list, 3)) # => 1

# 'None' means nil in Python. We use to indicate that the item wasn't found.
print (binary_search(my_list, -1)) # => None
