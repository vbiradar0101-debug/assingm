class House:
    def __init__(self, address, rooms, rent, color, owner):
        self.address = address
        self.rooms = rooms
        self.rent = rent
        self.color = color
        self.owner = owner

House1 = House("pune", 4, 2500, "gray","Raani")
House2 = House("pune", 3, 2000, "black","Vaishu")
House3 = House("mumbai", 2, 2500, "pink", "sonu")
House4 = House("Latur",3, 8000, "gray", "saraswati")
House5 = House("nanded",4, 1000, "green", "vaishnavi")

House_list = []
House_list.append(House1)
House_list.append(House2)
House_list.append(House3)
House_list.append(House4)
House_list.append(House5)

print("House list:  ")

for i in House_list:
    print("address: ", i.address)
    print("room: ", i.room)
    print("rent: ",i.rent)
    print("color: ",i.color)
    print("owner: ",i.owner)
    print("*************************")

