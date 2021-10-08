animals=['cat','dog','rabbit']
#adding by append
animals.append('pig')
print("list after append:",animals)

#adding by extend
wild_animal=['tiger','fox']
animals.extend(wild_animal)
print("list after  extend: ", animals)

#inserting 
animals.insert(3,'elephant')
print("list after insering at index 3:",animals)

#pop
animals.pop(3)
print("list after pop: ",animals)