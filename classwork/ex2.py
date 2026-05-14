class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return f"Restaurant: {self.restaurant_name} | Cuisine: {self.cuisine_type}"

restaurant1 = Restaurant("American dinner inn", "American")
restaurant2 = Restaurant("Sushi paradise", "Asian")
restaurant3 = Restaurant("Khinkali house", "Georgian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

print(f"Name: {restaurant1.restaurant_name}. Cusine: {restaurant1.cuisine_type}")
print(f"Name: {restaurant2.restaurant_name}. Cusine: {restaurant2.cuisine_type}")
print(f"Name: {restaurant3.restaurant_name}. Cusine: {restaurant3.cuisine_type}")