
def billing():
    l = list()
    total_price = 0
    n = int(input("Enter the value of n = "))
    for i in range(n):
        a = input("Do u want to add more products for billing?(Y/N)").upper()
        if a == "Y":
            product = input("Enter the product to purchase = ")
            quantity = int(input("Enter the quantity you want to purchase = "))
            product_price = int(input("Enter the price of the product = "))
            total = product_price * quantity
            total_price = total_price + total
        else:
            print("Bill price = " + str(total_price))
            break
billing()
