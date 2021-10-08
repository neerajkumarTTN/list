#string=['a','b','c','d','e']
#print(string)
#reversing list by slicing method
#new=string[::-1]
#print("by slicing method: ",new)

#reverse by using reverse
#string.reverse()
#print("reverse method:",string)

string=['a','b','c','d','e']
print(string)
 
L = len(string)
 
for i in range(int(L/2)):

    n = string[i]
    string[i] = string[L-i-1]
    string[L-i-1] = n
 
print(string)