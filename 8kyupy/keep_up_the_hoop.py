"""Alex just got a new hula hoop, he loves it but feels discouraged because his little brother is better than him

Write a program where Alex can input (n) how many times the hoop goes round and it will return him an encouraging message :)

If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".
If he doesn't get 10 hoops, return the string "Keep at it until you get it"."""

#My solution:
def hoop_count(n):
    return "Great, now move on to tricks" if n >= 10 else "Keep at it until you get it" #literally just return the string under given condtions


#Other solutions
def hoopCount(n):
    if n>=10:
        return 'Great, now move on to tricks'
    else:
        return 'Keep at it until you get it'

#For good measure
def hoopCount(n):
    # Good Luck!
    if n < 0:
        return "Really now...?"                    # Just in case
    
    elif n < 10:
        return "Keep at it until you get it"
    
    else:
        return "Great, now move on to tricks"