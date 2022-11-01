"""Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.

Task
Write a function that returns both the minimum and maximum number of the given list/array.

"""

#My solution...
def min_max(lst):
    return [min(lst),max(lst)]  #literally return an array of the minimum and maximum integers within the variable whatever is passed in

#Other Solution...
def min_max(lst):
  # Too easy, but requires two passes
  # return[min(lst), max(lst)]
  
  # Single pass:
  l, u = None, None
  for n in lst:
      if l is None or n < l:
          l = n
      if u is None or n > u:
          u = n
  return [l, u]
