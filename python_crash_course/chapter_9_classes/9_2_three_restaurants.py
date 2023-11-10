class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is open!")

restaurant1 = Restaurant('Victorino', 'European')
restaurant2 = Restaurant('Chat Noir', 'French')
restaurant3 = Restaurant('Nagoya', 'Japanese')


restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()


