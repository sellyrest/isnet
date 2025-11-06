import math as mt
import random as rm
# width = 0 
# length = 0
# area = 0

# def findArea(a,b):
#     result = a * b 
#     return result

# def findTriangle(a,b):
#     result = (a*b)/2
#     return result

# def findVolume(a,b,c):
#     vol = a * b * c
#     return vol

# area1 = findArea(200, 30)
# area2 = findArea(400, 40)
# area3 = findArea(500, 30)
# triangle1 = findTriangle(100,100)
# cube1 = findVolume(10, 20, 30)
# print('the area of rectangle is', area1, area2, area3, triangle1, cube1)


# def show_numbers():
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#     for x in numbers:
#         if x % 2 == 0:
#             print( x, '- even number')
#         else:
#             print( x, '- odd number')
# show_numbers()

# breadQty = 100
# teaQty = 100
# breadPrice = 15000
# teaPrice = 5000

# def show_stock():
#     print("\nWelcome to Sheseyz Shop ^^")

# def choose_product():
#     print("\nchoose what u want to buy:")
#     print("1. bread only")
#     print("2. tea only")
#     print("3. bread and tea")
#     choice = input("enter your choice (1/2/3): ")

#     numOfBread = 0
#     numOfTea = 0

#     if choice == '1':
#         numOfBread = int(input("how many bread do u want to buy? "))
#     elif choice == '2':
#         numOfTea = int(input("how many tea do u want to buy? "))
#     elif choice == '3':
#         numOfBread = int(input("how many breads? "))
#         numOfTea = int(input("how many teas? "))
#     else:
#         print("invalid choice :)")
#         return choose_product()

#     return numOfBread, numOfTea

# def calculate_payment(breadCount, teaCount, money):
#     totalPrice = (breadCount * breadPrice) + (teaCount * teaPrice)
#     totalReturn = money - totalPrice
#     freeBread = breadCount // 5
#     freeTea = teaCount // 5
#     return totalPrice, totalReturn, freeBread, freeTea

# def print_receipt(breadCount, teaCount, totalPrice, totalReturn, freeBread, freeTea):
#     print("\nRECEIPT")
#     print(f"total price: {totalPrice}")

#     if totalReturn > 0:
#         print(f"money return: {totalReturn}")
#     elif totalReturn < 0:
#         print(f"not enough money! you need {abs(totalReturn)} more.")
#     else:
#         print("exact amount paid.")

#     if freeBread > 0:
#         print(f"Bonus: {freeBread} free bread(s). Total bread: {breadCount + freeBread}")
#     if freeTea > 0:
#         print(f"Bonus: {freeTea} free tea(s). Total tea: {teaCount + freeTea}")

# def check_stock(breadCount, teaCount):
#     if breadCount > breadQty or teaCount > teaQty:
#         if breadCount > breadQty:
#             print(f"not enough bread :( we only have {breadQty}")
#         if teaCount > teaQty:
#             print(f"not enough tea :( we only have{teaQty}")
#         return False
#     return True

# while True:
#     show_stock()
#     breadCount, teaCount = choose_product()
#     money = int(input("how much money do u have?"))

#     if check_stock(breadCount, teaCount):
#         totalPrice, totalReturn, freeBread, freeTea = calculate_payment(breadCount, teaCount, money)
#         print_receipt(breadCount, teaCount, totalPrice, totalReturn, freeBread, freeTea)

#     again = input("\nbuy anothaa?? (y/n): ").lower()
#     if again != 'y':
#         print("ENJOYYY ^^")
#         break


# to get a bonus code
# free = 1 
# if qty == 6:
#     total = (price*qty)-(price*free)

# x = 8
# y = 5
# print(mt.log(x, y)) #
# print(mt.fabs(x))
# print(mt.asinh(x))
# print(mt.modf(x))
# print(mt.remainder(x, y))
# print(mt.copysign(x, y)) #Returns x with the sign of y
# print(mt.erf(x))
# print(mt.erfc(x))
# print(mt.trunc(x))

# q = 1
# r = 10
# val = 1
# bet = 1000
# if val == rm.randrange(q, r):
#     print('you win', bet * 10)
# else:
#     print('you lose your money')

import random as rm

q = 1
r = 10
val = int(input("💰 Guess a number between 1 and 10: "))
bet = 1000

lucky = rm.randrange(q, r + 1)
print(f"✨ The lucky number is {lucky}!")


if val == lucky:
    print(f"JACKPOT! You win {bet * 10:,} coins!")
elif abs(val - lucky) == 1:
    print(f"😁 So close! You win back half: {bet / 2:,} coins.")
else:
    print(f"😔 You lose {bet:,} coins. Better luck next time!")

def gauss_sum(n):
    total = n * (n + 1) // 2
    print(f"✨ The Gauss magic for 1 → {n} is: {total} 🎯")
    return total
gauss_sum(10)
gauss_sum(100)

