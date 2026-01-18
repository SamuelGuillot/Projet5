class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        aire = self.width * self.length
        return aire

    def calculate_perimeter(self):
        perimetre = 2 * (self.width + self.length)
        return perimetre


rectangle = Rectangle(5, 3)
print("Largeur:", rectangle.width)
print("Longueur:", rectangle.length)
print("Aire:", rectangle.calculate_area())
print("Périmètre:", rectangle.calculate_perimeter())
