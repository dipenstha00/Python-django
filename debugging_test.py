print("Hello")

def loop():
    a = 0
    for i in range(1,3):
        print(f"{i}")
        a = a * i
    print(f"the product is {a}")

pool = loop()
print(loop)