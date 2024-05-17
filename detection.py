#import setup_path 
import airsim
import cv2
import numpy as np 
import pprint
import sys
import math
import geo
import mgrs
from tabulate import tabulate

client = airsim.MultirotorClient()
client.confirmConnection()

camera_name = "0"
image_type = airsim.ImageType.Scene

client.simSetDetectionFilterRadius(camera_name, image_type, 200 * 100) 
# amosacnobi obieqtis saxeli
client.simAddDetectionFilterMeshName(camera_name, image_type, "Car*") 
    
mgrs_conv = mgrs.MGRS()

Artillery_coords = (42.164805, 44.078532)

while True:
    rawImage = client.simGetImage(camera_name, image_type)
    if not rawImage:
        continue
    png = cv2.imdecode(airsim.string_to_uint8_array(rawImage), cv2.IMREAD_UNCHANGED)
    targets = client.simGetDetections(camera_name, image_type)
    if targets:
        for target in targets:
            s = pprint.pformat(target)
            drone_state = client.getMultirotorState()

            # Mewinave Metvaltvalis lat,lon,alt
            FO_lat = client.getHomeGeoPoint('my_drone').latitude
            FO_lon = client.getHomeGeoPoint('my_drone').longitude
            FO_alt = client.getHomeGeoPoint('my_drone').altitude

            # Dronis gadaxra chrdiloetidan-dan, lat, lon, alt, mandzili miznamde 
            drone_orientation = int(math.degrees(2*math.acos(drone_state.kinematics_estimated.orientation.w_val))) 
            drone_lat = format(client.getGpsData(vehicle_name="my_drone").gnss.geo_point.latitude,'.6f')
            drone_lon = format(client.getGpsData(vehicle_name="my_drone").gnss.geo_point.longitude, '.6f')
            drone_alt = format(client.getGpsData(vehicle_name="my_drone").gnss.geo_point.altitude, '.0f')
            drone_distance_to_object = int(target.relative_pose.position.get_length())
            drone_mgrs = mgrs_conv.toMGRS(drone_lat, drone_lon)

            # Miznis lat,lon,alt
            target_lat = float(format(geo.obj_coordinates(drone_lat, drone_lon, drone_distance_to_object, drone_orientation)[0],'.6f'))
            target_lon = float(format(geo.obj_coordinates(drone_lat, drone_lon, drone_distance_to_object, drone_orientation)[1],'.6f'))
            target_alt = format(target.geo_point.altitude, '.0f')
            target_mgrs = mgrs_conv.toMGRS(target_lat, target_lon)

            distance_to_target = format(geo.distance(Artillery_coords[0], Artillery_coords[1], target_lat, target_lon), '.0f')
            fwd_azimuth_target = format(geo.bearing(Artillery_coords[0], Artillery_coords[1], target_lat, target_lon), '.0f')


            print(f"""         
    ZOGADI MONACEMEBI
===============================================================
    Artillery Lat,Lon : {Artillery_coords[0], Artillery_coords[1]}
    Artillery MGRS: {mgrs_conv.toMGRS(Artillery_coords[0], Artillery_coords[1])}
            
    Dronis Lat,Lon: {format(drone_lat), format(drone_lon)}
    Dronis MGRS: {drone_mgrs}
    Dronis gadaxra N-dan: {drone_orientation}°
    Dronis simagle: {drone_alt} m
    Mandzili dronidan miznamde: {drone_distance_to_object} m
            """)

            print(120 * "_")
            formatter_result = "{:<15} {:<15} {:<15} {:<15} {:<20} {:<15} {:<15}"
            print(formatter_result.format(*["Miznis ID", "Azimuti", "Mandzili", "Simagle", "MGRS", "Latitude", "Lontitude"]))
            results = [target.name, str(fwd_azimuth_target) + '°' , str(distance_to_target) + ' m', str(target_alt) + ' m', target_mgrs, target_lat, target_lon]
            print(formatter_result.format(*results))
            print(120 * "_")

            sys.stdout.flush()
            cv2.rectangle(png,(int(target.box2D.min.x_val),int(target.box2D.min.y_val)),(int(target.box2D.max.x_val),int(target.box2D.max.y_val)),(255,0,0),2)
            cv2.putText(png, target.name, (int(target.box2D.min.x_val),int(target.box2D.min.y_val - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36,255,12))

    cv2.imshow("Drone-Aided Artillery(DART): saartilerio dazverva", png)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('c'):
        client.simClearDetectionMeshNames(camera_name, image_type)
    elif cv2.waitKey(1) & 0xFF == ord('a'):
        client.simAddDetectionFilterMeshName(camera_name, image_type, "Car*")
cv2.destroyAllWindows() 


