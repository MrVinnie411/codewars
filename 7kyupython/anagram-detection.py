#The Problem
#An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

#Note: anagrams are case insensitive

#Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

# My Solution:Python
def is_anagram(test, original):
    pass
def is_anagram(test, original):
    return set(test.lower()) == set(original.lower()) and len(test) == len(original)

#other solutions...
def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower()) 

#for good measure
def is_anagram(test, original):
    test_dict, original_dict = {}, {}
    for i in test.lower():
        test_dict[i] = test_dict.get(i, 0) + 1
    for i in original.lower():
        original_dict[i] = original_dict.get(i, 0) + 1
        
    return test_dict == original_dict

