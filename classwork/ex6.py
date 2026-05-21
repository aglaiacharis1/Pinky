class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return f"Restaurant: {self.restaurant_name}, Cuisine: {self.cuisine_type}"

    def open_restaurant(self):
        return "Restaurant is open now!"
    
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors):
        super().__init__(restaurant_name, cuisine_type= "Ice cream")
        self.flavors = flavors

    def display_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(f"-{flavor}")

my_stand = IceCreamStand("Scooby-doo", ["vanilla", "chocolate", "strawberry"])
print(my_stand.describe_restaurant())
my_stand.display_flavors()