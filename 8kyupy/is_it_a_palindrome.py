"""Write a function that checks if a given string (case insensitive) is a palindrome.

"""
#My Solution
def is_palindrome(s):
    s = s.lower().replace(' ','')
    return s==s[::-1]

    """Set your variable to itself with the lower method appended with the replace method:

S= s.lower().replace(‘’,’ ‘)
*ensure you leave a space 

Then return your variable if  after, it goes thru the methods you appended to it ,it is equal to the reverse of itself 

return s == s[::-1]"""

#Other Solutions
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]



#For Good Measure...
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]
