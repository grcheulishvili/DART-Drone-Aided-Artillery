## Project setup instructions

Download [AirSimNH](https://github.com/microsoft/AirSim/releases/download/v1.8.1-windows/AirSimNH.zip) environment

download this folder and put it here: .\AirSimNH\WindowsNoEditor\\**code folder here**

*Anaconda Airsim env setup:*
>Anaconda-> Environments -> Import env : airsim-environment.yml

*Anaconda environment export(**if you want to share your new environment with others**):*
> Anaconda-> Environments -> Export env

running program:
> start_drone.bat


File Structure
-------------------- 
```
Airsim/
└── WindowsNoEditor/
    ├── AirSimNH
    ├── code/
    │   ├── airsim_environment.yml  -> anaconda env config file 
    │   ├── controller.py  -> drone manual controls
    │   ├── detection.py -> object detection and geolocation
    │   ├── README.md -> you are here
    │   ├── settings.json -> Airsim config file
    │   └── start_drone.bat -> run this in anaconda "airsim" environment
    ├── Engine
    └── AirsimNH.exe
```

*PIP dependencies*
```
1. msgpack-rpc-python
2. airsim
3. pynput
```


