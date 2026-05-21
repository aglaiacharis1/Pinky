class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        return f"Restaurant: {self.restaurant_name}, Cuisine: {self.cuisine_type}"

    def open_restaurant(self):
        return "Restaurant is open now!"
    
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, visitors):
        self.number_served += visitors



restaurant = Restaurant("American dinner inn", "American")
print(f"Initial customers served: {restaurant.number_served}")
restaurant.number_served = 20
print(f"Customers served after manual change: {restaurant.number_served}")

restaurant.set_number_served(50)
print(f"Customers served after set_number_served: {restaurant.number_served}")

restaurant.increment_number_served(100)
print(f"Total customers served after incriment: {restaurant.number_served}")