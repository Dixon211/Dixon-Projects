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
    def get_picture(self):
        if self.width >= 50 or self.height >= 50:
            return "Too big for picture."
        else:
            star_line = f"{'*'*self.width}\n"
            star_lines = star_line * self.height
            return star_lines
    #come back to this after making the square subclass
    def get_amount_inside(self):
        return None
class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        #super() allows this constructor to pull the variables from the rectangle parent class and distill them down for the Square
        # this allows us to set both the height and width, which should be the same to the self.side
        super().__init__(side, side)
    def __str__(self):
        sqr_print = f"Square(side={self.side})"
        return sqr_print
    def set_width(self, width):
        self.side = width
        self.width = width
        self.height = width
    def set_height(self, height):
        self.side = height
        self.width = height
        self.height =height
    



