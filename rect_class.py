class Rect:
    def __init__(self, w, h, o):
        self.width = w
        self.height = h
        self.outline = o

    def __str__(self):
        info = " width - " + str(self.width) 
        info += ", " + " Height - " + str(self.height)
        info += ", " + "Outline - " + self.outline
        return info

    def grow(self):
        if self.width < 15 and self.height < 15:
            self.width += 1
        self.height += 1   

    def shrink(self):
        if self.width > 3 and self.height > 4:
            self.width -= 1
            self.height -= 1

    def draw_top(self):
        for column in range(self.width):
            print(self.outline, end = "")
        print()

    def draw_middle(self):
        for row in range(self.width - 2):
            print(self.outline, end = "")
            for column in range(self.width - 2):
                print("  ", end = "")
            print(self.outline)
        

    def draw_bottom(self):
        for column in range(self.width):
            print(self.outline, end = "")
        print()

    def draw(self):
        self.draw_top()
        self.draw_middle()
        self.draw_bottom()

    def combine(self, rect2):
        new_width = self.width + rect2.width
        new_height = self.height + rect2.height
        new_outline =self.outline
        new_rect = Rect(new_width, new_height, new_outline)
        return new_rect
        
        
    

