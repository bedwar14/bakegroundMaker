from PIL import Image, ImageDraw
import io

BLACK, DARKGRAY, GRAY = ((0,0,0), (63,63,63), (127,127,127))
LIGHTGRAY, WHITE = ((191,191,191), (255,255,255))
BLUE, GREEN, RED = ((0, 0, 255), (0, 255, 0), (255, 0, 0))



class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    @staticmethod
    def from_point(other):
        return Point(other.x, other.y)


class Rect(object):
    def __init__(self, x1, y1, x2, y2):
        minx, maxx = (x1,x2) if x1 < x2 else (x2,x1)
        miny, maxy = (y1,y2) if y1 < y2 else (y2,y1)
        self.min = Point(minx, miny)
        self.max = Point(maxx, maxy)

    @staticmethod
    def from_points(p1, p2):
        return Rect(p1.x, p1.y, p2.x, p2.y)

    def __str__(self):
        return 'Rect({:d}, {:d}, {:d}, {:d})'.format(self.min.x, self.min.y,
                                                     self.max.x, self.max.x)
    width  = property(lambda self: self.max.x - self.min.x)
    height = property(lambda self: self.max.y - self.min.y)

class GradGen:
    def __init__(self):
        self.test1 = "7"
    def gradient_color(self, minval, maxval, val, color_palette):
        """ Computes intermediate RGB color of a value in the range of minval
            to maxval (inclusive) based on a color_palette representing the range.
        """
        max_index = len(color_palette)-1
        delta = maxval - minval
        if delta == 0:
            delta = 1
        v = float(val-minval) / delta * max_index
        i1, i2 = int(v), min(int(v)+1, max_index)
        (r1, g1, b1), (r2, g2, b2) = color_palette[i1], color_palette[i2]
        f = v - i1
        return int(r1 + f*(r2-r1)), int(g1 + f*(g2-g1)), int(b1 + f*(b2-b1))
    def horz_gradient(self, draw, rect, color_func, color_palette):
        minval, maxval = 1, len(color_palette)
        delta = maxval - minval
        for x in range(rect.min.x, rect.max.x+1):
            f = (x - rect.min.x) / float(rect.width)
            val = minval + f * delta
            color = color_func(minval, maxval, val, color_palette)
            draw.line([(x, rect.min.y), (x, rect.max.y)], fill=color)
    def vert_gradient(self, draw, rect, color_func, color_palette):
        minval, maxval = 1, len(color_palette)
        delta = maxval - minval
        for y in range(rect.min.y, rect.max.y+1):
            f = (y - rect.min.y) / float(rect.height)
            val = minval + f * delta
            color = color_func(minval, maxval, val, color_palette)
            draw.line([(rect.min.x, y), (rect.max.x, y)], fill=color)
    def Generate(self):
        color_palette = [BLUE, GREEN, GREEN]
        region = Rect(0, 0, 1400, 800)
        imgx, imgy = region.max.x+1, region.max.y+1
        image = Image.new("RGB", (imgx, imgy), WHITE)
        draw = ImageDraw.Draw(image)
        self.horz_gradient(draw, region, self.gradient_color, color_palette)
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        return img_byte_arr
        #image.show()
