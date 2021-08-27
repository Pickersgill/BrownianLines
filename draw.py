import classes
import style
import sys
import random
from PIL import Image, ImageDraw

Point = classes.Point
PointList = classes.PointList
Field = classes.Field

class DrawField:
    PART_COL = "#f01111"
    BG_COL = "#000000"
    def __init__(self, field):
        self.field = field
        self.img = Image.new("RGBA", (style.WIDTH, style.HEIGHT), color=style.BG_COL)
        self.draw = ImageDraw.Draw(self.img)
        self.draw.circle = \
            lambda x, y, rad, fill : self.draw.ellipse([(x-rad, y-rad), (x+rad, y+rad)] , fill=fill)

    def get_field_img(self):
        return self.img

    def draw_line_with_outline(self, points, colour, width):
        self.draw.line(points, style.HERO_OUTLINE_COL, width + (style.HERO_OUTLINE_WIDTH * 2))
        for point in points:
            self.draw.circle(point[0], point[1], (style.HERO_LINE_W // 2) + style.HERO_OUTLINE_WIDTH, \
            fill=style.HERO_OUTLINE_COL)

        self.draw.line(points, colour, width)
        for point in points:
            self.draw.circle(point[0], point[1], (style.HERO_LINE_W // 2), fill=colour)

    def render(self):
        for h in self.field.heroes:
            for trail in h.trails:
                if style.RANDOM_COL:
                    temp_col = random.choice(style.HERO_COLS)
                else:
                    temp_col = style.HERO_COL

                self.draw_line_with_outline(trail, temp_col, style.HERO_LINE_W)

if __name__ == "__main__":
    
    seed = random.randrange(sys.maxsize)

    if style.SEED:
        seed = style.SEED    
    
    print("Using seed: ", seed)

    field = Field(style.PARTICLE_NUM, style.HERO_NUM)
    draw = DrawField(field)
    
    field.sim(style.TIME)
    draw.render()
    draw.get_field_img().show()
    
