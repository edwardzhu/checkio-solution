import re, math


def circle_equation(note):
    points = [Point(x=p) for p in re.findall(r'\(\d+,\d+\)',note)]
    line1 = Line(points[0], points[1])
    line2 = Line(points[0], points[2])

    rx, ry = 0,0
    if line1.b is None:
        rx = line1.s
        ry = line2.s * rx + line2.b
    elif line2.b is None:
        rx = line2.s
        ry = line1.s * rx + line1.b
    else:
        rx = (line1.b - line2.b) / (line2.s - line1.s)
        ry = line1.s * rx + line1.b

    r = points[0].distance(Point(x=rx, y=ry))
    result ="(x-" + format_number(rx) + ")^2+(y-" + format_number(ry) + ")^2=" + format_number(r) + "^2"
    return result


def format_number(f):
    r = round(f,2)
    if int(r) == r:
        return repr(int(r))
    return repr(r)


class Point:
    def __init__(self, x, y = None):
        if y is None:
            parts = x.replace("(", "").replace(")", "").split(",")
            self.x = float(parts[0])
            self.y = float(parts[1])
        else:
            self.x = x
            self.y = y

    def find_midpoint(self, another):
        return Point(x=(self.x + another.x) /2, y=(self.y + another.y) / 2)

    def calc_slope(self, another):
        return (another.y - self.y) / (another.x - self.x)

    def distance(self, another):
        return math.sqrt((another.x - self.x) ** 2 + (another.y - self.y) ** 2)


class Line:
    def __init__(self, p1, p2):
        if p1.x == p2.x:
            self.s = 0
            self.b = (p1.y + p2.y)/2
        elif p1.y == p2.y:
            self.s = (p1.x + p2.x)/2
            self.b = None
        else:
            midpoint = p1.find_midpoint(p2)
            self.s = -1 / p1.calc_slope(p2)
            self.b = midpoint.y - self.s * midpoint.x

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert circle_equation("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert circle_equation("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
    assert circle_equation("(7,3),(9,6),(3,6)") == "(x-6)^2+(y-5.83)^2=3^2"

    print("Use 'Check' to earn sweet rewards!")
