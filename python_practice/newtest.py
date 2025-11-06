# x = 10

# # if x == 10: 
# #     print('first true,now we are inside the IF')
# # if x > 10: 
# #     print('second true,x is hingher than 10')
# # if x < 10: 
# #     print('third true, x is less than 10') 

#     print('IF is powerful') 

# name = 'mark'
# gender = 'male'
# age = 20
# ticketprice = 50000 
# ticketstock = 50
# day = 'saturday' 
# numofticket = 20 #try at home 
# numofticket_formale = 5
# numofticket_for_female = 5 
# ticketdiscount = ticketprice * 0.5 
# totalmale = numofticket_formale * ticketprice
# totalfemale = numofticket_for_female * ticketdiscount 
# grandtotalticket =  totalfemale + numofticket_formale  

# if ticketstock > 0:
#   if age > 17:
#    if gender =='female' or gender =='male':
#     print(name, 'you can watch the movie')
#   else: 
#    print(name, 'your not allowed')
# else: 
#  print('sorry', name , 'the ticket is not available') 

# if ticketstock > 0:
#   if age > 17:
#    if gender =='female' and day == 'saturday':
#     print(name, 'you have discount,', 'you must pay',ticketdiscount)
#   else: 
#    print(name, 'you must pay', ticketprice)
# else: 
#  print('sorry', name , 'the ticket is not available') 

# if ticketstock > 0:
#   if age > 17:
#    if gender =='male':
#     print(name, 'you must pay', ticketprice)
# else: 
#  print('sorry', name , 'the ticket is not available')

# if age > 17: 
#  if gender == 'male':
#   if numofticket > 1 and numofticket_formale > 0:
#    print('you buy more than 1, you must pay' , numofticket_formale * ticketprice)
#  else: 
#   print('you buy more! , you must pay' , numofticket_for_female + ticketdiscount)

# else: 
#  print('sorry, your not allowed')

# print('the total will be' , grandtotalticket)

# breadQty = 7
# teaQty = 20
# breadPrice = 15000
# teaPrice = 5000

# while True:
#     print("welcome to sheseyz shop ^^")
#     print("Stock available: Bread =", breadQty, "| Tea =", teaQty)

#     numOfBread = int(input("how many breads do you want to buy? "))
#     numOfTea = int(input("how many teas do you want to buy? "))
#     totalPay = int(input("how much money do you have? "))

#     totalPrice = (numOfBread * breadPrice) + (numOfTea * teaPrice)
#     totalReturn = totalPay - totalPrice

#     breadOnlyPrice = numOfBread * breadPrice
#     breadReturn = totalPay - breadOnlyPrice
#     teaOnlyPrice = numOfTea * teaPrice
#     teaReturn = totalPay - teaOnlyPrice

#     freeBread = numOfBread // 5
#     freeTea = numOfTea // 5

#     print("receipt")

#     if breadQty >= numOfBread and teaQty >= numOfTea:
#         print("Total price:", totalPrice)
#         print("Your change:", totalReturn)

#         if freeBread > 0:
#             print("BONUS! You get", freeBread, "free bread! Now you have", numOfBread + freeBread, "bread.")
#         if freeTea > 0:
#             print("BONUS! You get", freeTea, "free tea! Now you have", numOfTea + freeTea, "tea.")

#         breadQty -= numOfBread
#         teaQty -= numOfTea

#     elif breadQty >= numOfBread:
#         print("We only have", teaQty, "tea while you need", numOfTea)
#         print("But we still have enough bread!")
#         if numOfBread > 0:
#             print("Bread only? The price is", breadOnlyPrice, "| Your change:", breadReturn)

#     elif teaQty >= numOfTea:
#         print("We only have", breadQty, "bread while you need", numOfBread)
#         print("But we still have enough tea!")
#         if numOfTea > 0:
#             print("Tea only? The price is", teaOnlyPrice, "| Your change:", teaReturn)

#     else:
#         print("Oh no :(")
#         print("Bread available:", breadQty, "needed:", numOfBread)
#         print("Tea available:", teaQty, "needed:", numOfTea)
        
#     again = input("\ndo you want to buy another? (y/n): ").lower()
#     if again != 'y':
#         print("\nthank you for shopping! come again soon")
#         break

def show_numbers():
    numbers = [2, 4, 5, 6, 8, 10, 12, 14, 15, 16, 18, 20]
    i = 0

    while i < len(numbers):
        x = numbers[i]
        # to check odd or even number
        if x % 2 == 0:
            print('loop number', x, '- even number')
        else:
            print('loop number', x, '- odd number')

        i += 1
show_numbers()

# x = 1
# while x <= 4:
#     print(x)
#     x += 1
#     print(x)

# x = 'A'
# z = 1

# while z <= 3:
#     print(x * z)
#     z += 1

# myChar = 'A'
# x = 1
# z = 1

# while x < 2:
#     print(myChar*z)
#     x+=1
#     z+=1

# myChar = 'A'
# z = 4 

# while z >= 1:
#     print(myChar * z)
#     z -= 1
    
# myChar = 'A'
# space = ' '
# numA = 1
# numSpace = 4 

# while numA <= 5:
#     print(space * numSpace + myChar * (2 * numA - 1))
#     numA += 1
#     numSpace -= 1



# n = 5  # tinggi segitiga

# for i in range(n):
#     # spasi di depan (supaya segitiga rata tengah)
#     print(" " * (n - i - 1), end="")
#     # huruf 'A' berurutan sesuai pola
#     print("A" * (2 * i + 1))
 
n = 5  # tinggi segitiga

# 🔺 Segitiga atas (terbalik)
for i in range(n - 1, -1, -1):
    print(" " * (n - i - 1), end="")
    print("A" * (1 * i + 1))

# 🔻 Segitiga bawah (normal)
for i in range(1, n):
    print(" " * (n - i - 1), end="")
    print("A" * (1 * i + 1))

