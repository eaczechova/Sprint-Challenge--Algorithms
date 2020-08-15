#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
I's O(n) since the number it will run depends on n. 

b)
It's O(log n) since the number of operations changes.

c)
It is O(N) as the function has single recursive callstack and the inner function call is triggered by n. 
## Exercise II

Since, floors are a sorted list of numbers, I would first find "the middle floor" and checking if eggs breaks there.
If not, I would cut off the floors above (including "the middle floor") and find the new middle. 
Otherwise, I would cut off "the middle floor" and look for the f floor above the orignially found middle. 

It time complexity would be O(log n).
