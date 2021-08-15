from PIL import Image, ImageDraw
import random
import style
import math

WIDTH = style.WIDTH
HEIGHT = style.HEIGHT
MAX_SPEED = style.MAX_SPEED

class Point:
    def __init__(self, x=-1, y=-1, xvel=None, yvel=None, collision=False, rad=style.POINT_RAD, \
            mass=style.POINT_MASS):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel
        self.collision = collision
        self.rad = rad
        self.mass = mass

        if self.x < 0:
            self.x = random.randrange(0, WIDTH)
        if self.y < 0:
            self.y = random.randrange(0, HEIGHT)
        if self.xvel is None:
            self.xvel = random.randrange(-MAX_SPEED, MAX_SPEED)
        if self.yvel is None:
            self.yvel = random.randrange(-MAX_SPEED, MAX_SPEED)

    def tick(self):
        self.x += self.xvel
        self.y += self.yvel

    def __str__(self):
        return "Point: x=%d, y=%d" % (self.x, self.y)

class Hero(Point):
    def __init__(self):
        start_pos = self.num_to_perimeter(None)
        self.x = start_pos[0]
        self.y = start_pos[1]
        self.xvel = random.randrange(-style.MAX_HERO_SPEED, style.MAX_HERO_SPEED)
        self.yvel = random.randrange(-style.MAX_HERO_SPEED, style.MAX_HERO_SPEED)
        self.collision = True
        self.rad = style.HERO_RAD
        self.mass = style.HERO_MASS
        self.trails = [[]]
    
    def tick(self):
        self.x += self.xvel
        self.y += self.yvel 
        self.trails[-1].append((self.x, self.y))

    def new_trail(self):
        self.trails.append([])

    def num_to_perimeter(self, num):
        w = style.WIDTH
        h = style.HEIGHT
    
        if num is None:
            return self.num_to_perimeter(random.randint(0, w + w + h + h))
    
        num = num % (w + w + h + h)
        if num <= w:
            x = num
            y = 0
        elif num <= w + h:
            x = w
            y = num % w
        elif num <= w + w + h:
            x = w - num % (w + h)
            y = h
        elif num <= w + w + h + h:
            x = 0
            y = h - num % (w + w + h) 

        return (x, y)

class PointList(list):
    def __str__(self):
        return "[" + ", ".join(str(s) for s in self) + "]"


class Field:
    def __init__(self, num_parts=200, num_heroes=10):
        self.particles = self.gen_particles(num_parts)
        self.heroes = self.gen_heroes(num_heroes)
        self.hero_trail = []

    def gen_heroes(self, num):
        h = PointList()
        for i in range(num):
            h.append(Hero())
        return h

    def gen_particles(self, num):
        parts = PointList()
        for i in range(num):
            parts.append(Point())
        return parts

    def sim(self, ticks=1):
        for i in range(ticks):
            for p in self.particles:
                p.tick()
                self.collide(p)
            for h in self.heroes:
                h.tick()
                self.collide(h)

    def collide(self, c):
        edge = False
        if c.x > style.WIDTH:
            if c in self.heroes:
                c.x = 0
                c.new_trail()
            else:
                c.x = style.WIDTH
                c.xvel *= -1
        elif c.x < 0:
            if c in self.heroes:
                c.x = style.WIDTH
                c.new_trail()
            else:
                c.x = 0
                c.xvel *= -1
        elif c.y > style.HEIGHT:
            if c in self.heroes:
                c.y = 0
                c.new_trail()
            else:
                c.y = style.HEIGHT
                c.yvel *= -1
        elif c.y < 0:
            if c in self.heroes:
                c.y = style.HEIGHT
                c.new_trail()
            else:
                c.y = 0 
                c.yvel *= -1
   
        if c in self.heroes and edge:
            c.new_trail()

        if not c.collision:
            return 
        

        for p in filter(lambda x : x is not c, self.particles):

            dist = math.hypot(p.x - c.x, c.y - p.y)
            if dist < (c.rad + p.rad):
                m1 = c.mass
                m2 = p.mass
                dx1 = c.xvel
                dx2 = p.xvel
                dy1 = c.yvel
                dy2 = p.yvel

                newdx1 = (dx1 * (m1 - m2) + (2 * m2 * dx2)) / (m1 + m2)
                newdy1 = (dy1 * (m1 - m2) + (2 * m2 * dy2)) / (m1 + m2)
                newdx2 = (dx2 * (m2 - m1) + (2 * m1 * dx1)) / (m2 + m1)
                newdy2 = (dy2 * (m2 - m1) + (2 * m1 * dy1)) / (m2 + m1)

                c.xvel = newdx1
                c.yvel = newdy1
            
                p.xvel = newdx2
                p.yvel = newdy2
            
    def __str__(self):
        return "Field containing %d particles" % len(self.particles)


if __name__ == "__main__":
    field = Field()    
    print(field)
    print(field.particles)




