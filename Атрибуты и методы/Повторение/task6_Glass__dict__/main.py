class Glass:
    def __init__(self, capacity_volume: [int, float], occupied_volume: [int, float]):
        self.capacity_volume = capacity_volume  # объем стакана
        self.occupied_volume = occupied_volume  # объем жидкости в стакане

    def add_water(self, water):
        self.occupied_volume += water
        return self.occupied_volume

glass1 = Glass(500, 0)
glass2 = Glass(500, 100)
if __name__ == "__main__":
    glass = Glass(200, 100)
