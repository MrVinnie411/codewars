#Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

#It should remove all values from list a, which are present in list b keeping their order.

#arrayDiff([1,2],[1]) == [2]

#If a value is present in b, all of its occurrences must be removed from the other:

#arrayDiff([1,2,2,2,3],[2]) == [1,3]

# My Solution
def array_diff(a, b):
    return [i for i in a if i not in b] #This simply nests a for loop in an else statement by iterating over the array and checking to see if any values from the first variable array are in the second variable array

#Other Solutions
def array_diff(a, b):
    set_b = set(b)
    return [i for i in a if i not in set_b]

#For Good Measure...
def array_diff(a, b):
    #your code here
    return filter(lambda i: i not in b, a)
