#bulit in datatype store multiple values in single varible
#mutable
food=["gulamjamun","chlo","shre"]
print(len(food))
print(max(food))   
print(min(food))

#indexing 
marks=[99,100,90,95]

print(marks)

marks[0]=98 #change
print(marks)
print(marks[1:3]) #slicing
marks.append(92) #adding
print(marks)
marks.sort()  #sort
print(marks)


#strings are immutable
name="shree"
name[0]="h"
print(name)

#tuple cannot be changed