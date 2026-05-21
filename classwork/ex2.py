class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return f"Restaurant: {self.restaurant_name}, Cuisine: {self.cuisine_type}"

    def open_restaurant(self):
        return "Restaurant is open now!"


restaurant_1 = Restaurant("American dinner inn", "American")
restaurant_2 = Restaurant("Sushi Paradise", "Asian")
restaurant_3 = Restaurant("Khinkali House", "Georgian")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

print(f"Restaurant: {restaurant_1.restaurant_name}, Cuisine: {restaurant_1.cuisine_type}")
print(f"Restaurant: {restaurant_2.restaurant_name}, Cuisine: {restaurant_2.cuisine_type}")
print(f"Restaurant: {restaurant_3.restaurant_name}, Cuisine: {restaurant_3.cuisine_type}")
