
username = input('what is you name here ')
 ids = len(input('what is you password '))
lenght = ('*' * ids)

print(f'{username}, your password {lenght} is {ids} letters long')

#list

cart = ["you at cool",
        "you are awesome",
        "you are a waterboy",
        "milk is good"]
print (cart [0])
print (cart[0::2])

cart[0] = 'ice water'
cart_1 = cart[:]
cart_1 [1] = 'chicken'
print(cart)
print(cart_1)