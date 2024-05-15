#import setup_path 
import airsim
import cv2
import numpy as np 
import pprint
import sys


# connect to the AirSim simulator
client = airsim.VehicleClient()
client.confirmConnection()

# set camera name and image type to request images and detections
camera_name = "0"
image_type = airsim.ImageType.Scene

# set detection radius in [cm]
client.simSetDetectionFilterRadius(camera_name, image_type, 200 * 100) 
# add desired object name to detect in wild card/regex format
client.simAddDetectionFilterMeshName(camera_name, image_type, "Car*") 


while True:
    rawImage = client.simGetImage(camera_name, image_type)
    if not rawImage:
        continue
    png = cv2.imdecode(airsim.string_to_uint8_array(rawImage), cv2.IMREAD_UNCHANGED)
    cars = client.simGetDetections(camera_name, image_type)
    if cars:
        for car in cars:
            s = pprint.pformat(car)
            print(f"""\r
            Afrenis Lat,Lon,Alt: {client.getHomeGeoPoint('my_drone').latitude}, {client.getHomeGeoPoint('my_drone').longitude}, {client.getHomeGeoPoint('my_drone').altitude} m
            Amjamindeli Lat,Lon: {format(client.getGpsData(vehicle_name="my_drone").gnss.geo_point.latitude,'.5f'), format(client.getGpsData(vehicle_name="my_drone").gnss.geo_point.longitude, '.5f')}
            
            Avtomobili
            ----------------
            Manqanis ID: {car.name} 
            Mandzili obieqtamde:  {car.relative_pose.position.get_length()} m
            Koordinati: 

            DroneState: {client.simGetGroundTruthKinematics('my_drone')}
            """)
            sys.stdout.flush()

            cv2.rectangle(png,(int(car.box2D.min.x_val),int(car.box2D.min.y_val)),(int(car.box2D.max.x_val),int(car.box2D.max.y_val)),(255,0,0),2)
            cv2.putText(png, car.name, (int(car.box2D.min.x_val),int(car.box2D.min.y_val - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36,255,12))

    cv2.imshow("AirSim dronis virtualuri chveneba", png)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('c'):
        client.simClearDetectionMeshNames(camera_name, image_type)
    elif cv2.waitKey(1) & 0xFF == ord('a'):
        client.simAddDetectionFilterMeshName(camera_name, image_type, "Car*")
cv2.destroyAllWindows() 
