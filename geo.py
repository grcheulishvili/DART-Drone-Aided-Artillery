import geopy
from geopy.distance import geodesic
import geopy.distance
import pyproj

# obieqtis koordinatebis gamotvla 
def obj_coordinates(my_lat, my_lon, d, bearing):
    origin = geopy.Point(my_lat, my_lon)
    destination = geodesic(d).destination(origin, bearing)

    lat2, lon2 = destination.latitude, destination.longitude

    return lat2, lon2

# mandzilis gamotvla koordinatebs shoris
def distance(lat1, lon1, lat2, lon2):
    coords_1 = (lat1, lon1)
    coords_2 = (lat2, lon2)
    return geopy.distance.geodesic(coords_1, coords_2).m

# azimutis gasagebad
def bearing(lon1, lat1, lon2, lat2):
    geodesic = pyproj.Geod(ellps='WGS84')
    fwd_azimuth,back_azimuth,distance = geodesic.inv(lon1, lat1, lon2, lat2)
    return fwd_azimuth