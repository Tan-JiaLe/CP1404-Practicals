total = 0
DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.9

number_of_item = int(input("Number of items: "))
while number_of_item < 0:
    print("Invalid Input")
    number_of_item = int(input("Number of items: "))

for i in range(number_of_item):
    price = float(input(f"Enter price of item {i+1} : $"))
    total += price

if total > DISCOUNT_THRESHOLD:
    total = total * DISCOUNT_RATE

print(f"Total price for {number_of_item} items is {total:.2f}")
