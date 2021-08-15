import classes
import style
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

    def render(self):
        for h in self.field.heroes:
            for trail in h.trails:
                self.draw.line(trail, style.HERO_COL, style.HERO_LINE_W)

field = Field(style.PARTICLE_NUM, style.HERO_NUM)
draw = DrawField(field)

field.sim(style.TIME)
draw.render()
draw.get_field_img().show()

