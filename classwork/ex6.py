class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return f"Restaurant name is: {self.restaurant_name} Cuisine is: {self.cuisine_type}"

    def open_restaurant(self):
        return f"{self.restaurant_name} is open now!"

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors):
        super().__init__(restaurant_name, cuisine_type="Ice Cream")
        self.flavors = flavors

    def display_flavors(self):
        print(f"Availble flavors: {self.flavors}")

my_stand = IceCreamStand("Scooby-Doo ice-cream", ["Vanilla", "Chocolate", "Strawberry"])
print(my_stand.describe_restaurant())
my_stand.display_flavors()

restaurant = Restaurant("American diner inn", "American")


print(f"Name: {restaurant.restaurant_name}")
print(f"Cusine: {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()