#The Problem

#Write a function that returns a string in which firstname is swapped with last name.

#My Solution
def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])

#other solutions...
def name_shuffler(str_):
    [first, last] = str_.split()
    return last + " " + first

#for good measure...
name_shuffler = lambda s: ' '.join(reversed(s.split()))