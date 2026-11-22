class Plant:
    def __init__(self, name, height, age_days):
        """Initialize a Plant instance."""
        self.name = name
        self.age_days = age_days
        self.height = height  # in centimeters

    def grow(self):
        """Simulate the growth of the plant over one day."""
        self.height += 1
        self.age_days += 1

    def age(self):
        """Return the age of the plant in days."""
        return self.age_days

    def get_info(self):
        """Return information about the plant."""
        return f"{self.name} is {self.age_days} days old and {self.height} cm tall."

if __name__ == "__main__":
    print("welcome to my plant growth simulator")
    plants = [
        Plant("Rose", 10, 5),
        Plant("Tulip", 15, 3), 
        Plant("Sunflower", 20, 7)
    ]

    heights = {}

    for plant in plants:
        heights[plant.name] = plant.height

    for plant in plants:
        plant.get_info()


    print("Growing plants for 5 days...")
    
    for _ in range(5):
        for plant in plants:
            plant.grow()
            plant.age()

    print("Final plant information after growth:")
    for plant in plants:
        plant.get_info()
        growth = plant.height - heights[plant.name]
        print(f"{plant.name} grew by {growth} cm.")