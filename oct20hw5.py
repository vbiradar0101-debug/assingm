
class Bus:
    def __init__(self, number, name, capacity, driver, price):
        self.number = number
        self.name =  name
        self.capacity = capacity
        self.driver = driver
        self.price = price

bus1 = Bus("MH12AB1234", "Shivneri", 45, "Rahul", 500)
bus2 = Bus("MH14CD5678", "Shivshahi", 40, "Amit", 400)
bus3 = Bus("MH20EF9012", "Volvo", 50, "Rohan", 450)
bus4 = Bus("MH24GH3456", "School Bus", 35, "Suresh", 20)
bus5 = Bus("MH31IJ7890", "City Bus", 60, "Vijay", 30)

print("Bus list :")

Bus_list = []
Bus_list.append(bus1)
Bus_list.append(bus2)
Bus_list.append(bus3)
Bus_list.append(bus4)
Bus_list.append(bus5)

for i in Bus_list :
    print("bus number : ",i.number)
    print("name : ",i.name)
    print("capacity : ",i.capacity)
    print("driver : ",i.name)
    print("tikit price : ",i.price)
    print("**************************")


    

