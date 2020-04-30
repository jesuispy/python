store = ["some string", 1234, "test"] #example list with intergers

print(store)

store.append("addition to list") #adding item to list
print(store)

store.pop()
print(".pop last value from list", store) #remove last item on list

print(len(store)) #displays lenght of var store

print(store[0]) #display items in list count starts from 0

#dictonary key and value

diction = {"fruit": "banana",
          "cereal": "oatmeal",
          "drink": "water"}
print("All values in the dictionary are", diction)
print("Values under fruit are", diction['fruit'])
diction["fruit"] = "apple" #update value in dictionary
print("All values in the dictionary are", diction)

#tuples are 2 value pairs
tups = "item1", "item2", "item3", "item4"

print(tups[3])
