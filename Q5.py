list=[1,1,1,1,1,2,1,1,2,1,2,4,2,1,3,4]	 
max1,max2,max3=0,0,0 
for i in list:	 
    if i>max1:	 
        max3=max2 
        max2=max1 
        max1=i 
    elif i>max2:	 
        max3=max2 
        max2=i 
    elif i>max3:	 
        max3=i 
print("The second maximum element in the list is", max2)
print("The Third maximum element in the list is",max3) 