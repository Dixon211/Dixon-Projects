class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width
    
    def __str__(self):
        rect_print = f"Rectangle:(width={self.width}, height={self.height})"
        return rect_print
    
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2*(self.width)+2*(self.height)
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    # need to set 50+ clause
    def get_picture(self):
        star_line = f"{'*'*self.width}\n"
        star_lines = star_line * self.height
        return star_lines
    def get_amount_inside(self):
        return None


practice_rect = Rectangle(6, 8)
print(practice_rect.get_picture())