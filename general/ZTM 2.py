
money = 100
print("how much money is it", money)
money -= 2 #augmented assignment operator used
print("say what",money)
money += 2 #augmented assignment operator used
print("You sure",money)

first_name = input("what is you first name ")
print(type(first_name))

name1 = "test "
name2 = "me"
wholename = name1 + name2
print(wholename)
print(name1 + name2) #string concatenation
print(str(10000)) #string type
print(type(str(10000)))
print(int(100))
print(type(int(100)))
x = str(10) #long way
y = int(x)
z = type(y)
print(z)


actor = 'Malcom'
age = 20
print(f'Hi {actor}. You are {age} years old')
print(len(actor)) #len is lenght count start from 1 not 0
#method
alphabeth = 'i will code soon'
print(alphabeth.upper())
print(alphabeth.capitalize())
print(alphabeth.find("will"),"is the starting point")

print(alphabeth.replace("will", "learnt")) #replace

birth_year = int(input("What year were you born "))
age = 2019 - birth_year
print(f'your age us: {age}')



