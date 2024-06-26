## Project Preview
![Program in motion](https://github.com/grcheulishvili/AirsimDrone-Experiment/blob/main/preview.PNG)

## Project setup instructions

Download [AirSimNH](https://github.com/microsoft/AirSim/releases/download/v1.8.1-windows/AirSimNH.zip) environment

download this repo and put it here: .\AirSimNH\WindowsNoEditor\\**code folder here**

*Anaconda Airsim env setup:*
> Anaconda > Environments> Import > import airsim_environment.yml

*Anaconda environment export(**if you want to share your new environment with others**):*
> Anaconda > Environments > Export > export airsim_environment.yml

running program (in anaconda prompt):
> activate airsim

*navigate to AirsimDrone-Experiment/ folder*

> start_drone.bat


File Structure
-------------------- 
```
Airsim/
└── WindowsNoEditor/
    ├── AirSimNH
    ├── AirsimDrone-Experiment/
    │   ├── airsim_environment.yml  -> anaconda env config file 
    │   ├── controller.py  -> drone manual controls
    │   ├── detection.py -> object detection and geolocation
    |   ├── geo.py -> functions related to geoprocessing
    │   ├── README.md -> you are here
    │   ├── settings.json -> Airsim config file
    │   └── start_drone.bat -> run this in anaconda "airsim" environment
    ├── Engine
    └── AirsimNH.exe
```

## PIP Dependencies
> pip install mgrs geopy pyproj



