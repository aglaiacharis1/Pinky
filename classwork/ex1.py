class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return f"Restaurant: {self.restaurant_name}, Cuisine: {self.cuisine_type}"

    def open_restaurant(self):
        return "Restaurant is open now!"


restaurant = Restaurant("American dinner inn", "American")

print(f"Restaurant: {restaurant.restaurant_name}")
print(f"Cuisine: {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()