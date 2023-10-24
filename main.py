class HouseBuilder:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating the house builder...")
            cls._instance = super(HouseBuilder, cls).__new__(cls)
            cls.walls = 0
            cls.doors = 0
            cls.windows = 0
            cls.roof = False
        return cls._instance

    def add_wall(self):
        self.walls += 1
        print(f"Added a wall. Total walls: {self.walls}")

    def add_door(self):
        self.doors += 1
        print(f"Added a door. Total doors: {self.doors}")

    def add_window(self):
        self.windows += 1
        print(f"Added a window. Total windows: {self.windows}")

    def add_roof(self):
        if not self.roof:
            self.roof = True
            print("Added the roof.")
        else:
            print("The house already has a roof.")

    def build_house(self):
        if self.walls >= 4 and self.doors >= 1 and self.windows >= 1 and self.roof:
            print("The house has been built successfully!")
        else:
            print("Incomplete house. Please add more parts.")

if __name__ == "__main__":
    builder_1 = HouseBuilder()
    builder_2 = HouseBuilder()

    print(builder_1 is builder_2)  # Output: True

    builder_1.add_wall()
    builder_1.add_door()
    builder_2.add_window()
    builder_2.add_roof()

    builder_2.build_house()
