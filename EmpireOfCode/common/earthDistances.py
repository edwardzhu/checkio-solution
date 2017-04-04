import math, re
R = 6371

def distance(first, second):
    s, f = parse_point(first), parse_point(second)
    r = math.acos(math.sin(s[0]) * math.sin(f[0]) + math.cos(s[0]) * math.cos(f[0]) * math.cos(s[1] - f[1]))
    result = r * R
    return result


def parse_point(point):
    latitude, longitude = re.findall(r"\d+°\d+′\d+″[SNEW]", point)
    result = parse_degree(latitude.strip(" ,")), parse_degree(longitude.strip(" ,"))
    return result


def parse_degree(degree):
    d, m, s = degree[:-1].replace(u"°", " ").replace(u"′", " ").replace(u"″", " ").strip().split(" ")
    d2 = float(d) + float(m) / 60 + float(s) / 3600
    return get_factor(degree) * math.radians(d2)


def get_factor(degree):
    if degree.endswith("E") or degree.endswith("N"):
        return 1
    else:
        return -1

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(
        distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2), "From Greenwich to Geneva"
    assert almost_equal(
        distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1), "From South to North"
    assert almost_equal(
        distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2), "Opera Night"

    distance("48°27′0″N,34°59′0″E", "15°47′56″S 47°52′0″W")

    print("All done? Earn rewards by using the 'Check' button!")