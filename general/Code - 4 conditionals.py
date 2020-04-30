print(True)
print(False)
print(True==True)
print(True==False)

print("5","Justin"=="Justin")
print("6","justin"=="Justin")

example_1 = ["I","am","home"]
example_2 = ["I","am","home"]
example_3 = ["I","am","out"]

print("7", example_1==example_3)
print("8", example_1==example_2)
print("9", not example_3==example_1)
print("10", not example_3 is example_1)

print("11 length is ",len(example_1))
print("12 compared length to 6 is ", len(example_1)==6)
print("13 compared length to 3 is ", len(example_1)==3)
print("14 compared length greater than or equal to 3 is ", len(example_1)>=3)
print("15 compared length less than 3 is ", len(example_1)<3)

listnum = [2,4,6,8]
for y in listnum:
    print("number ", y)

for y in listnum:
    print("squared ", y**2)


for y in listnum:
    if y == 8:
        print("correct it\'s 8")
    elif y == 2:
        print("choose again")
    else:
        print(y)

