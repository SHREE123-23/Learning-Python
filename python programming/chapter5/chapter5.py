# dictonary in python :store datatype 
# last value of key
student={"name":"shree",
         "age":"19",
         "city":"Miraj",
         "nav":"shree"}

print(type(student))
print(student)
print(student["name"])

student["city"]="sangli"  #changes in keys
print(student)

student["fav"]="maths"      #add new keys
print(student)

student.pop("fav")
print(student)            #remove key


print(student.keys())     #see all keys


#Sets in pyhton 
food ={"panner","gulabjamun","bulat"}
print(food)
food.add("hu")          #add 
print(food)         
food.remove("hu")
print(food)

#empty set
#empty= set()
#print(type(empty))