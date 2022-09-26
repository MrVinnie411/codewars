"""Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.

Square all numbers k (0 <= k <= n) between 0 and n.

Count the numbers of digits d used in the writing of all the k**2.

Call nb_dig (or nbDig or ...) the function taking n and d as parameters and returning this count."""

#My solution

def nb_dig(n, d):
    '''Takes an integer n, calculates the square of each number from one to n, and returns
    how many times d appears'''
    
    values_list = list(range(0, n+1))
    list_squared = list(map(lambda x: str(x**2), values_list))
    str_list_squared = ''.join(list_squared)
    print(str(d))
    return str_list_squared.count(str(d))

#Other solutions
def nb_dig(n, d):
    return sum(str(i*i).count(str(d)) for i in range(n+1))

#For Good measure
def nb_dig(n, d):
    y=[]
    dollamakemeholla = 0
    for i in range(0, n+1):
        y.append(i*i)
    #print y
    
    for jk in y:
        for t in str(jk):
            if(t == str(d)):
                dollamakemeholla += 1
    print dollamakemeholla
    return dollamakemeholla