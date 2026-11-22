"""Plant class and its subclasses."""

class Plant:
    """A class representing a plant."""

    def __init__(self, name, height, age_days):
        """Initialize the plant with a name, height, and age."""
        self.name = name
        self.height = height
        self.age_days = age_days

    def get_info(self):
        """Return a string with the plant's information."""
        return f"Plant Name: {self.name}, Height: {self.height} cm, Age: {self.age_days} days"

class Flower(Plant):
    """A class representing a flower, which is a type of plant."""

    def __init__(self, name, height, age_days, color):
        """Initialize the flower with a name, height, age, and color."""
        super().__init__(name, height, age_days)
        self.color = color

    def get_info(self):
        """Return a string with the flower's information."""
        return f"Flower Name: {self.name}, Height: {self.height} cm, Age: {self.age_days} days, Color: {self.color}"
    def bloom(self):
        """Simulate the flower blooming."""
        return f"The {self.name} is blooming with beautiful {self.color} petals!"
class Tree(Plant):
    """A class representing a tree, which is a type of plant."""

    def __init__(self, name, height, age_days, species):
        """Initialize the tree with a name, height, age, and species."""
        super().__init__(name, height, age_days)
        self.species = species

    def get_info(self):
        """Return a string with the tree's information."""
        return f"Tree Name: {self.name}, Height: {self.height} cm, Age: {self.age_days} days, Species: {self.species}"
    def grow(self):
        """Simulate the tree growing taller."""
        self.height += 10  # Increase height by 10 cm
        return f"The {self.name} has grown to {self.height} cm tall!"
class Vegetable(Plant):
    """A class representing a vegetable, which is a type of plant."""

    def __init__(self, name, height, age_days, edible_part):
        """Initialize the vegetable with a name, height, age, and edible part."""
        super().__init__(name, height, age_days)
        self.edible_part = edible_part

    def get_info(self):
        """Return a string with the vegetable's information."""
        return f"Vegetable Name: {self.name}, Height: {self.height} cm, Age: {self.age_days} days, Edible Part: {self.edible_part}" 
    def harvest(self):
        """Simulate harvesting the vegetable."""
        return f"The {self.name} has been harvested! Enjoy the {self.edible_part}!"
    
if __name__ == "__main__":
    # Create instances of each plant type
    flowers = [
        Flower("Rose", 30, 15, "Red"),
        Flower("Tulip", 25, 10, "Yellow"),
    ]
    trees = [
        Tree("Oak", 500, 3650, "Quercus"),
        Tree("Pine", 600, 4000, "Pinus"),
    ]
    vegetables = [
        Vegetable("Carrot", 20, 30, "Root"),
        Vegetable("Lettuce", 15, 20, "Leaf"),
    ]

    for flower in flowers:
        print(f"{flower.name}: {flower.get_info()}")
        print(flower.bloom())   
    for tree in trees:
        print(f"{tree.name}: {tree.get_info()}")
        print(tree.grow())
    for vegetable in vegetables:
        print(f"{vegetable.name}: {vegetable.get_info()}")
        print(vegetable.harvest())