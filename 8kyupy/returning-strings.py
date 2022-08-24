#Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

#My Solution
def greet(name):
    #Good Luck (like you need it)
    pass
    return "Hello, "+ name+ " how are you doing today?"

#other solutions

    def greet(name):

        return "Hello, {} how are you doing today?".format(name)

#for good measure

greet = lambda name: f'Hello, {name} how are you doing today?'    