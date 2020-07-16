class Point:
    """Represents a point in 2-D space. """
    # def print_point(p):
    #     print('(%g, %g)' % (p.x, p.y))

class Rectangle:
    """Represents a rectangle.
    attributes: width, height, corner.
    """
if __name__ == "__main__":
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0
