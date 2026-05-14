class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return f"Restaurant name is: {self.restaurant_name}"
        return f"Cuisine is: {cuisine_type}"

    def open_restaurant(self):
        return f"{self.restaurant_name} is open now!"

restaurant = Restaurant("American diner inn", "American")


print(f"Name: {restaurant.restaurant_name}")
print(f"Cusine: {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()