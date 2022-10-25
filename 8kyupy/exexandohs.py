#Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

#My Solution:
def xo(s):
    return s.lower().count('x') == s.lower().count('o')
    
     #very simply you are returning your variable set to .lower(): which is a method that returns a string where all characters are lower case NEXT, you are counting the number of "x's" in your variable. Then,you are setting that equal to your variable.lower() again and then counting the number of "o's"


# Other Solution:
def xo(s):

  exes = 0
  ohs = 0

  for c in s.lower():
    if c == 'x':
      exes += 1
    elif c == 'o':
      ohs += 1

  return exes == ohs

