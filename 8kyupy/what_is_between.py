"""Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

"""

# My solution
def between(a,b):
    finalArray = [];
    for value in range(a, b + 1):
        finalArray.append(value);
    return finalArray



#other solutions

 def between(a,b):
    return list(range(a,b+1))



#FOr Good Measure
def between(a,b):
    arr = []
    for i in range(a, b + 1):
        arr.append(i)
    return arr

