import geopy
from geopy.distance import geodesic

def obj_coordinates(my_lat, my_lon, d, bearing):
    origin = geopy.Point(my_lat, my_lon)
    destination = geodesic(d).destination(origin, bearing)

    lat2, lon2 = destination.latitude, destination.longitude

    return lat2, lon2