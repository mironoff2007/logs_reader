import math
class Coordinates_converter:

    def CalcXCoord(lon1,lat1,lon2,lat2):

        R = 6371000

        f1 = lat1 * math.pi / 180;
        f2 = lat2 * math.pi / 180;
        df = (lat2 - lat1) * math.pi / 180;
        dl = (lon2 - lon1) * math.pi / 180;  # x

        a_x = math.cos((f1 + f2) / 2) * math.cos((f1 + f2) / 2) * math.sin(dl / 2) * math.sin(dl / 2);

        c_x = 2 * math.atan2(math.sqrt(a_x), math.sqrt(1 - a_x));

        d_x = R * c_x;

        if lon2 < lon1: d_x = -d_x

        return d_x

    def CalcYCoord(lon1, lat1, lon2, lat2):

        R = 6371000

        f1 = lat1 * math.pi / 180;
        f2 = lat2 * math.pi / 180;
        df = (lat2 - lat1) * math.pi / 180;
        dl = (lon2 - lon1) * math.pi / 180;  # x

        a_y = math.sin(df / 2) * math.sin(df / 2) + math.cos(f1) * math.cos(f2) * math.sin(0) * math.sin(0);

        c_y = 2 * math.atan2(math.sqrt(a_y), math.sqrt(1 - a_y));

        d_y = R * c_y;
        if lat2 < lat1: d_y = -d_y

        return d_y

    def calcDist(lon1,lat1,lon2,lat2):
        R = 6371000

        f1 = lat1 * math.pi / 180;
        f2 = lat2 * math.pi / 180;
        df = (lat2 - lat1) * math.pi / 180;
        dl = (lon2 - lon1) * math.pi / 180;  # x

        a = math.sin(df / 2) * math.sin(df / 2) + math.cos(f1) * math.cos(f2) * math.sin(dl / 2) * math.sin(dl / 2);

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a));

        d = R * c
        return d