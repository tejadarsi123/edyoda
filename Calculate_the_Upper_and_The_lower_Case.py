def count_function(s):
    lower = 0
    upper = 0
    for c in s:
        if(c.isupper()):
            upper+=1
        if(c.islower()):
            lower+=1
    return lower,upper

string = input("string : ")
lower,upper = count_function(string)
print("No. of Upper case characters :",upper)
print("No. of Lower case Characters :",lower)