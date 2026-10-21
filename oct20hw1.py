class Laptop:
    def __init__(self, n, p, b, c):
        self.name = n
        self.price = p
        self.brand = b
        self.color = c

pro1  = Laptop("Samsung", 70000, "Samsung", "gray")
pro2  = Laptop("Dell", 80000, "Dell", "black")
pro3  = Laptop("HP", 60000, "HP","silver")
pro4  = Laptop("Lenovo", 50000, "Lenovo", "black")
pro5  = Laptop("Samsung",80000, "Samsung", "black") 

Laptop_list = []
Laptop_list.append(pro1)
Laptop_list.append(pro2)
Laptop_list.append(pro3)
Laptop_list.append(pro4)
Laptop_list.append(pro5)

print("Laptop List:")

for i in Laptop_list:
    print("Name:", i.name)
    print("Price:", i.price)
    print("Brand:", i.brand)
    print("Color:", i.color)
    print("*********************")