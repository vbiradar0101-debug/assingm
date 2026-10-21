class pen:
    def __init__(self, n, p, c):
        self.name = n
        self.price = p
        self.color = c

pro1 = pen("gel", 20, "blow")
pro2 = pen("bright", 10, "black")
pro3 = pen("3D pen", 500, "red")
pro4 = pen("dip pen", 20, "blow")
pro5 = pen("marker", 50, "pink")
print("pen list :")

pen_list = []

pen_list.append(pro1)
pen_list.append(pro2)
pen_list.append(pro3)
pen_list.append(pro4)
pen_list.append(pro5)

for i in pen_list:
    print("pen name :", i.name )
    print("pricr :", i.price )
    print("color :", i.color )
    print("_______________________")
